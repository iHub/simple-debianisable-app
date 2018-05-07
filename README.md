### Installing the app.

Start by building the package


```
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install devscripts python-virtualenv git equivs python-dev dh-make git-buildpackage dh-virtualenv -y
dpkg-buildpackage

```

Then install the generated `.deb` file.

```
dpkg -i ../simple-app_1.0_amd64.deb 

```

Enjoy !
