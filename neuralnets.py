import numpy as np
import utilities as utils


class Classifier:
    """
    Generic classifier interface; returns random classification
    Assumes y in {0,1}, rather than {-1, 1}
    """

    def __init__(self, parameters={}):
        """ Params can contain any useful parameters for the algorithm """
        self.params = {}

    def reset(self, parameters):
        """ Reset learner """
        self.resetparams(parameters)

    def resetparams(self, parameters):
        """ Can pass parameters to reset with new parameters """
        try:
            utils.update_dictionary_items(self.params, parameters)
        except AttributeError:
            # Variable self.params does not exist, so not updated
            # Create an empty set of params for future reference
            self.params = {}

    def getparams(self):
        return self.params

    def learn(self, Xtrain, ytrain):
        """ Learns using the traindata """

    def predict(self, Xtest):
        probs = np.random.rand(Xtest.shape[0])
        ytest = utils.threshold_probs(probs)
        return ytest


class NeuralNet(Classifier):
    def __init__(self, parameters={}):
        self.params = {'nh': 4,
                       'transfer': 'sigmoid',
                       'stepsize': 0.01,
                       'epochs': 10}
        self.reset(parameters)

    def reset(self, parameters):
        self.resetparams(parameters)
        if self.params['transfer'] is 'sigmoid':
            self.transfer = utils.sigmoid
            self.dtransfer = utils.dsigmoid
        else:
            # For now, only allowing sigmoid transfer
            raise Exception('NeuralNet -> can only handle sigmoid transfer, must set option transfer to string sigmoid')
        self.wi = None
        self.wo = None

    def learn(self, Xtrain, ytrain):

        self.ni = Xtrain.shape[1]
        self.numberOfFeatures = Xtrain.shape[1]
        self.outPutNode = 1
        self.wi = np.random.normal(0, 1, self.numberOfFeatures * self.params['nh']).reshape(self.params['nh'],
                                                                                            self.numberOfFeatures)
        self.wo = np.random.normal(0, 1, self.params['nh'] * self.outPutNode).reshape(self.outPutNode,
                                                                                      self.params['nh'])

        for i in range(self.params['epochs']):
            dataPointIndexList = np.arange(Xtrain.shape[0])
            stepSize = self.params['stepsize'] / (i + 1)
            np.random.shuffle(dataPointIndexList);
            for index in dataPointIndexList:
                self.updateWeights(Xtrain[index, :], ytrain[index], stepSize)

    def derivativeOfSigmoid(self, sigmoidValues):
        """ Gradient of standard sigmoid 1/(1+e^-x) """
        return sigmoidValues * (1 - sigmoidValues)

    def updateWeights(self, samplePoint, trueLable, stepSize):
        (ah, a0) = self._evaluate(samplePoint)
        delta2 = np.multiply(a0, 1 - a0) * (a0 - trueLable)
        delta1 = delta2 * self.derivativeOfSigmoid(ah)
        self.wo = np.subtract(self.wo, stepSize * delta2)
        self.wi = np.subtract(self.wi.T, stepSize * delta1)
        self.wi = self.wi.T

    def predict(self, Xtest):
        ytest = []
        for i in range(Xtest.shape[0]):
            (ah, a0) = self._evaluate(Xtest[i, :])
            if a0 >= 0.5:
                ytest.append(1)
            else:
                ytest.append(0)
        return ytest

    # TODO: implement learn and predict functions


    def _evaluate(self, inputs):
        """ 
        Returns the output of the current neural network for the given input
        The underscore indicates that this is a private function to the class NeuralNet
        """
        if inputs.shape[0] != self.ni:
            raise ValueError('NeuralNet:evaluate -> Wrong number of inputs')

        # hidden activations
        ah = self.transfer(np.dot(self.wi, inputs))

        # output activations
        ao = self.transfer(np.dot(self.wo, ah))

        return (ah, ao)