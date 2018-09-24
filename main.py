import re
import math
import pprint

pp = pprint.PrettyPrinter(indent=4)

class NaiveBayesClassifier:

    Features = {}
    Records = []
    DsicreteProbability = {}
    ContinousData = {}
    Class = {}

    # constructor
    def __init__(self, filename = 'data.csv'):
        data = self.__getDataFromFile(filename)
        self.Features = data['features']
        self.Records = data['records']
        self.Class = self._getClass(self.Records)

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
        Class = {}
        for record in Records:
            Class[record[4]] = Class.get(record[4], 0) + 1
        return Class

    # get priors probability
    def __getPrior(self,Class):
        return self.Class[Class] / len(self.Records)

    # calculate mean
    def __mean(self, numbers):
        return sum(numbers) / float(len(numbers))

    # calculate variance
    def __variance(self, numbers):
        avg = self.__mean(numbers)
        variance = sum([pow(x - avg, 2) for x in numbers]) / float(len(numbers))
        return variance
        
    # calculate likelihoodDiscreate
    def getLikelihoodDis(self, indexFitur, valueFitur, kelas) :
        if indexFitur != 1 and indexFitur != 2 :
            raise Exception('parameter fitur harus index 1 atau 2')
        banyakFitur = 0
        banyakKelas = self.Class[kelas]
        for baris in self.Records :
            if baris[indexFitur] == valueFitur and baris[4] == kelas:
                banyakFitur += 1
        return banyakFitur / banyakKelas

    def getFitursValuesByClass(self,indexFitur,kelas):
        numbers = []
        for baris in self.Records :
            if baris[4] == kelas :
                numbers.append(float(baris[indexFitur]))
        return numbers

 # calculate likelihoodContinues
    def getLikelihoodCon(self,indexFitur,fiturValue,kelas):
        if indexFitur != 0 and indexFitur != 3:
            raise Exception('index fitur harus index 0 atau 3')
        numbers = self.getFitursValuesByClass( indexFitur, kelas )
        vars = self.__variance(numbers)
        mean = self.__mean(numbers)
        return 1 / math.sqrt( 2 * math.pi * vars ) * math.exp( - math.pow( fiturValue - mean ,2) / 2 * vars )
    
    # fiturValues adalah nilai dari yang diuji dalam bentuk array 1 dimensi
    def getPosterior(self,fiturValues, kelas):
        likelihood = self.getLikelihoodCon(0,fiturValues[0],kelas)
        likelihood = likelihood *self.getLikelihoodDis(1,fiturValues[1],kelas)
        likelihood = likelihood * self.getLikelihoodDis(2,fiturValues[2],kelas)
        likelihood = likelihood *self.getLikelihoodCon(3,fiturValues[3],kelas)
        return likelihood * self.__getPrior(kelas)

        #perhitungan kategori
    def hitung(self, fiturValues):
        posmiskin = self.getPosterior(fiturValues, 'miskin')
        possedang = self.getPosterior(fiturValues, 'sedang')
        poskaya = self.getPosterior(fiturValues, 'kaya')
        
        if posmiskin>possedang and posmiskin>poskaya:
            return "Miskin"
        elif possedang>posmiskin and possedang > poskaya:
            return "Sedang"
        elif poskaya>posmiskin and poskaya>possedang:
            return "Kaya"
        else:
            return "Tidak dapat diprediksi"
    
Trainer = NaiveBayesClassifier()
print(Trainer.hitung([15,'kayu bakar','ubin',6]))
