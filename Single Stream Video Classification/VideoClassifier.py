'''! party07 !'''

import VideoPooling as VP

class VideoClassifier:
    # resembles the top level video classifier
    # contains an architecture such as:
    # CNN --> Pooling to get video representation --> Classifier (FCN or SVM or whatever)
    # Ensure that dimensions match at the intersections...
    # CNN_Model: Fully Convolutional Network for local feature extraction, needs function forward
    # Pool_Vid_Rep: Pool for transfer from frame level to video level
    # Classifier: returns the predictions
    
    def __init__(self, CNN_Model, Pool_Strat, Classifier):
        self.CNN_Model = CNN_Model
        self.Pool_Vid_Rep = Pool_Strat
        self.Classifier = Classifier
        
    def forward(self, data):
        # takes data of dimension (#frames, height, width, rgb)
        
        xout = self.CNN_Model.forward(data)
        
        if self.Pool_Vid_Rep == 'average':
            xout = VP.average_pooling(xout)
        
        xout = self.Classifier.forward(xout)
        
        return xout
    
    def pooling(self, data):
        
        if self.Pool_Vid_Rep == 'average':
            xout = VP.average_pooling(data)
        
        return xout
        