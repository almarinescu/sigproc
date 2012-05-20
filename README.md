# Description

This project defines the methods for a bandpass filter and provides a UI
where the user can select the cutoff frequencies.

The project is distributed under the 'sigproc' (signal processing) python
package. Under this package there are 4 files:
 - control = the web application controller. This file maps URLs to python
   methods and provides the necessary logic to access the model.
 - model = the web application model. This file contains the database
   caching layer.
 - sig = signal processing related methods. This file contains methods to
   generate the coefficients for low-pass, high-pass and band-pass filters.
 - utils = various utility methods. This file contains the caching logic and
   the necessary methods to access the View templates.

# Installation

Create a python virtual environment:

```
virtualenv --no-site-packages sigproc
```

Make sure the newly create virtual environment is activated. Then clone
this repository:

```
git clone git://github.com/almarinescu/sigproc.git ~/sigproc
```

Install the sigproc package in the newly created virtual env:

```
python ~/sigproc/setup.py install
```

I personally had problems installing scipy using setuptools. If you
encounter troubles while running the above command. Try to run first 

```
easy_install -U numpy
```
and then run again the sigproc setup.py install method.

Sigproc uses memcache as one of it's caching layers, therefore make sure
you launch a memcache before you start sigproc. If you don't have a
memcache server running, sigproc will complain and refuse to start.

```
memcached -m 64 -p 1122 -u nobody -l 127.0.0.1
```

Launch the sigproc web-app:

```launch-sigproc```

The sigproc web-app should be up and running at 127.0.0.1:8080.

# Future developments

Logging various events and profile the performance of various components. A
configuration module would also be useful. Another improvement could be
done on the client side. We could cache results in the client's browser and
hit the server caching layer only when it's necessary.

