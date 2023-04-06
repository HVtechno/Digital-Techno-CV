# Digital-Techno-CV

In this repository, I have made a custom webapp using streamlit to digitized CV
Below I have discussed step-by-step procedure of this project implementation
- Create a Streamlit webapp using VSCODE
- Deploy the app in Render platform (which is an open source & free web hosting platform)
- create a nodejs script to awake your website after every 10 min so it wont sleep constently.

## Process Steps
1. First, Install the streamlit python library

```python
pip install streamlit
```
Once you installed the library, Define your folder structure as per below

```bash
├── .streamlit
│   ├── config.toml
├── assets   
│   ├── achieve2.png
│   ├── CV.docx
│   ├── CV.pdf
│   ├── profile-pic.png
├── styles
│   ├── main.css
├── app.py
├── Procfile
├── README.md
├── requirements.txt
├── setup.sh
```

2. Test your web app in your local machine with the following command
and pushed the codes in new Github respository. Finally, create a new account in render platform and deploy

```python
streamlit run app.py
```

## Youtube Materials for Reference
I would highly recommand to watch the youtube videos for the mentioned descriptive steps in order to avoid confusions on the process steps
* More details about [Build a Steamlit Webapp (Preview)
](https://www.youtube.com/watch?v=BXAeMICmUSQ)
* More details about [Render web hosting (Preview)
](https://www.youtube.com/watch?v=4SO3CUWPYf0)
* More details about [cron-job](https://console.cron-job.org/) create cron job & setup an HTTP call after 14 minute
