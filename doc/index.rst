.. Al3xBrs-OC-Lettings documentation master file, created by
   sphinx-quickstart on Thu Nov 23 11:10:08 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Al3xBrs-OC-Lettings's documentation!
===============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`Description`
* :ref:`Instruction`
* :ref:`Quick Start`
* :ref:`Technologies and languages`
* :ref:`Interfaces`
* :ref:`How to use`
* :ref:`Deploy and gesture`


.. _Description:
Description
===========

The project aims to discover the right structure and the deployment of an app on Django.
Data migration and CI/CD pipeline will be the core of the project.

.. _Instruction:
Instruction
===========

* Be sur to have Python 3.11 and git installed on your machine.

* Clone the repository on your machine ::

   git clone [repository]

* Create env ::

   python -m venv venv

* Install requirements ::

   pip install -r requirements.txt



.. _Quick Start:
Quick Start
===========

* Run the server ::

   python manage.py runserver

* Build Docker Image ::

   docker build -t [username-dockerhub]/[img-name]:[tag] .

* Run Docker Image ::

   docker run [username-dockerhub]/[img-name]:[tag]

* Push Docker Image ::

   docker push [username-dockerhub]/[img-name]:[tag]

.. _Technologies and languages:
Technologies and Languages
==========================

* Python v. 3.11
* Django
* sqlite3
* Docker
* CircleCi
* Sentry

.. _Structure and database:
Structure and Database
======================

The project has 3 apps.

* lettings :
   Everything about lettings and their address.
   An address model looks like ::

      class Address(models.Model):
          """
          Address model.
          Create an address.
          """

          number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
          street = models.CharField(max_length=64)
          city = models.CharField(max_length=64)
          state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
          zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
          country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

   A letting model looks like ::

      class Letting(models.Model):
       """
       Letting model.
       Create a letting with an address previously created.
       """

       title = models.CharField(max_length=256)
       address = models.OneToOneField(Address, on_delete=models.CASCADE)

* oc_lettings_site :
   Is the core of the project. It has settings.py and urls.py from the main project.

* profiles :
   Everything about profiles.
   A profile model looks like ::

      class Profile(models.Model):
       """
       Profile model.
       Create a new profile with a User django and a favorite_city.
       """

       user = models.OneToOneField(User, on_delete=models.CASCADE)
       favorite_city = models.CharField(max_length=64, blank=True)

.. _Interfaces:
Interfaces
=========

* Docker :
   Docker is use to build an image from the entire app. It can be deploy on any service.

* CircleCi :
   CircleCi is use to check tests from all commits from any branch.
   A docker image is build and deploy automatically only on master branch if tests covered more than 80% of the code.

* Render :
   Render is use to deploy the docker Image from a WebHook url.

* Sentry :
   Sentry is use to check any errors on your app.

.. _How to use:
How To Use
==========

If you have to commit any change, you have to check circleci status and be aware of any errors.

You can deploy a Docker Image on your machine using Docker Desktop. Docker Desktop has an user friendly interface that permits you to understand what is done.
To install Docker Image, go to : `https://www.docker.com/products/docker-desktop/`.

If you need to change your Sentry DSN, you can add a SENTRY_DNS variable in the Render .env file.

.. _Deploy and gesture:
Deploy and Gesture
==================

To deploy a new docker image on render. You have to commit on master branch.


