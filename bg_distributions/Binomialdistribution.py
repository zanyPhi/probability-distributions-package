import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Binomial(Distribution):

        
    """ Binomial distribution class for calculating and 
        visualizing a Binomial distribution.
        
        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats to be extracted from the data file
            p (float) representing the probability of an event occurring
                    
    """

        
    def __init__(self, prob = 0.5, size = 20):
   
        self.p = prob
        self.n = size
             
        super().__init__(self.calculate_mean(), self.calculate_stdev())
 

    def calculate_mean(self):

        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        
        self.mean = self.p * self.n

        return self.mean


    def calculate_stdev(self):
        
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        
        self.stdev = math.sqrt((self.p*self.n)*(1-self.p))

        return self.stdev


    def replace_stats_with_data(self):

        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        self.n = len(self.data)
        self.p = 1.0 * sum(self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        
        return self.p, self.n

    
    def plot_bar(self):

        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """

        plt.bar(x = ['0', '1'], height = [((1 - self.p)*self.n), (self.p*self.n)])
        plt.title('Binomial probability chart')
        plt.xlabel('Possible outcomes')
        plt.ylabel('No of outcomes')
        plt.show()
    
    
    def pdf(self, k):

        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        nCk = math.comb(self.n, k)
        pdf = nCk * math.pow(self.p, k) * math.pow(1-self.p, self.n-k)
        return pdf


    def plot_pdf_bar(self):

        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """

        prob = self.p
        size = self.n

        x = []
        y = []

        for k in range(0, self.n+1, 1):
            tmp = self.pdf(k)
            x.append(k)
            y.append(tmp)

        plt.bar(x, y)
        plt.xlabel('Number of successes')
        plt.ylabel('Probability of success')
        plt.title('Plot of binomial distribution density function')
        plt.show()


    def __add__(self, other): 

        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.p = self.p
        result.n = self.n + other.n
        result.mean = (result.n) * result.p
        result.stdev = math.sqrt(result.mean * (1 - self.p))
        
        return result
        
                                
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        
        return f"mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}"
        
        