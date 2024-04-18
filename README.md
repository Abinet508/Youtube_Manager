# YouTube Manager

> This script is a Python class for managing YouTube videos and playlists using the `pytube` and `googleapiclient` libraries.

## Prerequisites

> - Python 3.6 or higher
> - pytube library
> - moviepy library
> - google-auth library
> - google-auth-httplib2 library
> - google-auth-oauthlib library
> - google-api-python-client library

> > You can install these libraries using pip.

## Usage

> 1. Import the `YouTubeManager` class from the `youtube_manager.py` file.
> 2. Create an instance of the `YouTubeManager` class. You can optionally pass a YouTube URL and a file path to the constructor.

> > The `YouTubeManager` class has several methods for managing YouTube videos and playlists. Here are some examples:

> - `get_youtube(url)`: Returns a YouTube object for the given URL.
> - `get_playlist(url)`: Returns a Playlist object for the given URL.
> - `create_path(path)`: Creates a directory at the given path if it doesn't already exist.
> - `get_service()`: Returns a Google API service object.

## Credentials

> This script uses a service account for authentication with the Google API. You need to provide a JSON file with your service account credentials. By default, the script expects this file to be located at `./credentials/Service_credentials.json`.

> > Note: This is a basic usage guide. The actual usage may vary depending on the specific requirements of your project. Always refer to the source code for the most accurate information.

# Download Secure Files

> This script downloads secure files from GitLab to a specified directory.

## Usage

> The script is intended to be used with GitLab CI/CD.

> 1. Add a new job to your `.gitlab-ci.yml` file.
> 2. Set the `SECURE_FILES_DOWNLOAD_PATH` environment variable to the desired directory.
> 3. Use `curl` to download the script from this repository and execute it.


## Google Service Credentials

> The script is intended to be used with GitLab CI/CD.

> 1. Add a new job to your `.gitlab-ci.yml` file.
> 2. Set the `SECURE_FILES_DOWNLOAD_PATH` environment variable to the desired directory.
> 3. Use `curl` to download the script from this repository and execute it.

```yaml
secure_files_download:
  stage: download
  variables:
    SECURE_FILES_DOWNLOAD_PATH: "./credentials"
  script:
    - curl --silent "https://gitlab.com/gitlab-org/incubation-engineering/mobile-devops/download-secure-files/-/raw/main/installer" | bash
```

## Google Service Credentials

To use this script, you'll need to obtain service credentials from Google. Here's how you can do it:

> 1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

> 2. Create a new project or select an existing one.

> 3. In the sidebar on the left, go to APIs & Services > Library.

> 4. Search for 'Google Drive API', select the entry, and click 'ENABLE'.

> 5. Go to APIs & Services > Credentials.

> 6. Click on 'Create Credentials' and select 'Service account'.

> 7. Follow the prompts to create a new service account and download the JSON file.

> 8. Rename the downloaded JSON file to 'Service_credentials.json' and place it in the 'credentials' directory of this project.

