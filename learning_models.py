from typing import Dict
from numpy import ndarray


class LearningModel(object):

    def __init__(self, config_dct: Dict):
        self._config_dct = config_dct

    def fit(self, x: ndarray, y: ndarray) -> None:
        pass

    def predict(self, x: ndarray) -> ndarray:
        pass


class SVR(LearningModel):

    from sklearn.svm import SVR as sl_SVR

    def __init__(self, config_dct):
        super(SVR, self).__init__(config_dct)

        self.model = SVR.sl_SVR(kernel=self._config_dct["kernel"], verbose=self._config_dct["verbose"])

    def fit(self, x, y):
        self.model.fit(x, y)

    def predict(self, x):
        return self.model.predict(x)


class LR(LearningModel):

    from sklearn.linear_model import LinearRegression as sl_LR

    def __init__(self, config_dct):
        super(LR, self).__init__(config_dct)

        self.model = LR.sl_LR(n_jobs=self._config_dct["n_jobs"])

    def fit(self, x, y):
        self.model.fit(x, y)

    def predict(self, x):
        return self.model.predict(x)


if __name__ == "__main__":
    pass