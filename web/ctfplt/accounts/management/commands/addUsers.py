import argparse
import csv
from django.core.management.base import BaseCommand
from accounts.models import User, Affiliate
from problems.models import Problem

class Command(BaseCommand):
    help = "something anything"

    def add_arguments(self, parser):
        parser.add_argument('userList', type=argparse.FileType('r'))
        parser.add_argument('problemList', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        reader = csv.reader(options['problemList'])
        header = next(reader)
        problemList = []
        for row in reader:
            problem = Problem.objects.filter(title__exact=row[0])
            if len(problem) == 1:
                problemList += [problem[0]]

        reader = csv.reader(options['userList'])
        header = next(reader)
        for row in reader:
            username = row[0]
            userID = row[1]
            password = row[2]
            affiliateName = row[3]
            user = User.objects.create_user(username, '', password)
            user.userID = userID
            affiliate = Affiliate.objects.filter(name__exact=affiliateName)
            if len(affiliate) == 1:
                user.affiliate = affiliate[0]
            user.save()
            user.addAvailableProblems(problemList)
