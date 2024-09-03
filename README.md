# TypeAid -- The Intelligent Assistive Typing Platform

TypeAid revolutionizes typing for individuals who face challenges with traditional keyboards. Our assistive typing platform and text editor provide a seamless and effortless typing experience, empowering users with accessibility needs to effortlessly express themselves.

## Demo Video

Demo has been uploaded on Youtube: https://www.youtube.com/watch?v=_xoNV70jrjY

## Table of Contents

1. [Repository](#demo)

2. [Installation](#installation)

3. [Start Application](#repro)

<a name="demo"></a>

## 1. Repository

### What to find where

```bash
repository
├── backend // Backend system
│   ├── authentication // Where user profiles are handled
│   │   └── migrations
│   ├── backend
│   ├── predictive_text // Where the predictive text is handled
│   │   ├── datasets // Our dataset used for text prediction
│   │   └── migrations
│   ├── textHandler // Where files can be handled on stored on the backend database, currently unused.
│   │   └── migrations
│   └── userpreferences // Handle simple user preferences call, can reset, edit or add new user settings.
│       └── migrations
└── frontend // What you see
    ├── public
    │   └── assets // Images used to decorate the site icons, etc.
    │       └── images
    │           ├── png
    │           ├── shapes
    │           └── svg
    └── src
        ├── components // components such keyboard functionality
        ├── css
        ├── fonts // font used
        │   └── poppins
        └── views // each page on the site
```

<a name="installation"></a>

## 2. Installation

To install, make sure to have Python, and Node JS installed onto the machine and run the following commands (Each section assumes you are in the root directory of this repository):

```bash
git clone https://github.com/sfu-cmpt340/TypeAid.git
cd TypeAid
```

Frontend:

```bash
cd frontend
npm install
```

Backend:

```bash
cd backend
pip3 install -r requirements.txt
python3 manage.py migrate
```

<a name="repro"></a>

## 3. Start Application

To launch the application, start the backend and frontend server:

Frontend:

```bash
cd frontend
npm react-scripts start --host 0.0.0.0
```

Backend:

```bash
cd backend
python3 manage.py runserver
```
