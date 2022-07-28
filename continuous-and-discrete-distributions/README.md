# bg_distributions package

This is a python package that can be used to analyse and visualize binomial and gaussian distributions. 

    - Create Binomial(p, n) and Gaussian(mu, sigma) objects
    - Calculate mean, standard deviation and probability density function: 
        - Binomial.calcualate_mean(), Binomial.calculate.stdev(), Binomial.pdf()
        - Gaussian.calculate_mean(), Gaussian.calculate_stdev(sample = True), Gaussian.pdf(x) ---(sample = False for population standard deviation)
    - Visualize distribution:
        - Binomial.plot_bar(), Binomial.plot_pdf_bar()
        - Gaussian.plot_histogram(), Gaissian.plot_histogram_pdf(n_spaces)
    - Extract data from file:
        - Binomial.read_data_fiel(filename), Binomial.replace_data_with_stats()
        - Gaussian.read_data_file(filename)
    - Add objects and return new mean and standard deviation e.g. result = binomial1 + binomial2

# Files
    - bg_distributions/__init__.py: initialize importing objects
    - bg_distributions/Binomialdistribution.py: contains the Binomial child class
    - bg_distributions/Generaldistribution.py: contains the Distribution parent class
    - bg_distributions/Gaussiandistribution.py: contains the Gaussian child class
    - bg_distributions/license.txt
    - bg_distributions/README.md
    - bg_distributions/setup.cfg
    - numbers_binomial.txt
    - numbers.txt
    - requirements.txt
    - setup.py
    - test.py

# Installation

pip install bg_distributions
