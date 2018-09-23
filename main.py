import re
import math
import pprint

pp = pprint.PrettyPrinter(indent=4)

class NaiveBayesClassifier:

    Features = {}
    Records = {}
    DsicreteProbability = {}
    ContinousData = {}
    Class = {}

    # constructor
    def __init__(self, filename = 'data.csv'):
        data = self.__getDataFromFile(filename)
        self.Features = data['features']
        self.Records = data['records']
        self.Class = self._getClass(self.Records)
        prior = self.__getPrior(self.Records, self.Class)
        self.DiscreteProbability = self._generateDiscreteProbability(self.Records, self.Class)
        pp.pprint(self.DiscreteProbability)

    # get dataset from csv file
    def __getDataFromFile(self, filename):
        file = open(filename, 'r')
        features = file.readline()
        features = [feature.strip().lower() for feature in features.split(';')]
        table = file.readlines()
        records  = []
        for row in table:
            row = row.split(';')
            record = []
            for column in row:
                column = column.strip().lower()
                if re.match(r"\d+", column):
                    column = float(column)
                record.append(column)
            records.append(record)
        file.close()
        return {
            'features': features,
            'records': records,
        }

    # get class type
    def _getClass(self, Records):
        categories = set([record[4] for record in Records])
        Class = {}
        for record in Records:
            Class[record[4]] = Class.get(record[4], 0) + 1
        return Class

    # get priors probability
    def __getPrior(self, Records, Class):
        Class = {}
        for record in Records:
            Class[record[4]] = Class.get(record[4], 0) + 1 / len(Records)
        return Class

    # get likelihood and evidence from fixed data value
    def _generateDiscreteProbability(self, Records, Class):
        likelihood = {}
        evidence = {}
        for index, category in enumerate(Class):
            likelihood[category] = {}
        for record in Records:
            for index, featureValue in enumerate(record[:-1]):
                if type(featureValue) == str:
                    likelihood[record[4]][featureValue] = likelihood[record[4]].get(featureValue, 0) + 1 / Class[record[4]]
                    evidence[featureValue] = evidence.get(featureValue, 0) + 1 / len(Records)
        return {
            'likelihood': likelihood,
            'evidence': evidence
        }

    # calculate mean
    def __mean(self, numbers):
        return sum(numbers) / float(len(numbers))

    # calculate deviation standard
    def __stdev(self, numbers):
        return math.sqrt(self.__variance(numbers))

    # calculate variance
    def __variance(self, numbers):
        avg = self.__mean(numbers)
        variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers) - 1)
        return variance

    def __continousLikelihood(self, x, numbers):
        variance = self.__variance(numbers)
        avg = self.__mean(numbers)
        return 1 / math.sqrt( 2 * math.pi * variance) * math.exp(-(pow(x - avg, 2)) / 2 * variance)

Trainer = NaiveBayesClassifier()






