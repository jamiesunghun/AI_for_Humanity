from statistics import *
import openpyxl

class DataHandler:
    evaluator = Stat()
    
    @classmethod
    def get_data_from_excel(cls, filename):
        dic = {}
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        g = ws.rows
        
        for name, score in g:
            dic[name.value] = score.value
        
        return dic
    
    def __init__(self, filename, year_class):
        self.rawdata = DataHandler.get_data_from_excel(filename)
        self.year_class = year_class
        # 연산한 값을 저장해두는 저장소
        # 필요할 때 연산한되 이미 연산된 값이면 연산없이 저장된 값을 반환
        self.cache = {}
        
    def get_scores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = list(self.rawdata.values())
        return self.cache.get('scores')
    
    def get_average(self):
        if 'average' not in self.cache:
            self.cache['average'] = self.evaluator.average(
                self.get_scores())
            
        return self.cache.get('average')
    
    def get_variance(self):
        if 'variance' not in self.cache:
            self.cache['variance'] = self.evaluator.variance(
                self.get_scores(), self.get_average()
            )

        return self.cache.get('variance')
    
    def get_standard_deviation(self):
        if 'standard_deviation' not in self.cache:
            self.cache['standard_deviation'] = self.evaluator.std_dev(
                self.get_variance()
            )
        
        return self.cache.get('standard_deviation')

    def evaluate_class(self, total_avrg, sd):
        avrg = self.get_average()
        std_dev = self.get_standard_deviation()
        
        if avrg < total_avrg and std_dev > sd:
            print("성적 저조, 편차 너무 큼")
        elif avrg > total_avrg and std_dev > sd:
            print("성적 평균이상, 편차 큼")
        elif avrg < total_avrg and std_dev < sd:
            print("성적 저조, 편차 적음")
        elif avrg > total_avrg and std_dev < sd:
            print("성적 평균이상, 편차 적음")
        
    def get_evaluation(self, total_avrg, sd = 20):
        print('*' * 50)
        print('{} 반 성적 분석 결과'.format(self.year_class))
        print('{0} 반의 평균은 {1}점이고 분산은 {2}점이며 따라서 표준편차는 {3}이다'.format(
            self.year_class,
            self.get_average(),
            self.get_variance(),
            self.get_standard_deviation()))
        print('*' * 50)
        print('{}반 종합 평가'.format(self.year_class))
        print('*' * 50)
        self.evaluate_class(total_avrg, sd)