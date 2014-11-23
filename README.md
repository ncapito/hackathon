## Installation the app locally
1.  Pick a place to unpack everything (baseDir).  eg: Desktop/hackathon
1.  Download the [AppEngineSDK](https://cloud.google.com/appengine/downloads ) and unzip it to baseDir/AppengineSDK
1.  Download Python2.7.6 (if its not already installed.  Do not get 2.7.7 it will not work) and unpack it to baseDir/Python27
1.  Download [Windows Git](https://windows.github.com/)
1.  Optional:  Install [Sublime Text]( http://www.sublimetext.com/) (you need to use the standalone version).  Unpack to baseDir/Sublime


#Configuration
1.  Checkout the source from [Hackathon](https://github.com/ncapito/hackathon.git) .  Find  a tutorial online for this one :https://help.github.com/articles/getting-started-with-github-for-windows/
1.  Launch the App Engine SDK
1.  Click Preferences.  Set the Pyhon27 & AppengineSDK Path Above
1.  Open an Existing project


## Run the app locally

To run the app locally:

1. Open the Appengine SDK and click run
2. Launch via command line:
```
dev_appserver.py .
```


## Deploying

To deploy the application:

1. You can use the Appengine SDK Console.  Just click the app and hit publish.
1. Or can deploy via console:

```
appcfg.py update .
```
