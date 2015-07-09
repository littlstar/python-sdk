"""
Littlstar Python SDK

Copyright 2015 Little Star Media, Inc.

Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.

@author Wells Johnston <wells@littlstar.com>
"""

import requests
import urllib
import json

class SDK(object):

  BASE_URL = 'https://littlstar.com/api/v1/'

  def __init__(self, apikey = ''):
    self.apikey = apikey

  def search(self, endpoint, query, count = 30, page = 1):
    """Search Littlstar for photos, videos, users, channels, or everything"""
    uri = 'search'
    if (endpoint != 'all'):
      uri += '/' + endpoint
    options = { 'q': query, 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_user(self, user_id):
    """Get a user by id or slug"""
    uri = 'users/' + user_id
    return self.make_request(uri)

  def get_user_videos(self, user_id, count = 30, page = 1):
    """Get a user's videos"""
    uri = 'users/' + user_id + '/videos'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_user_photos(self, user_id, count = 30, page = 1):
    """Get a user's photos"""
    uri = 'users/' + user_id + '/photos'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_user_channels(self, user_id, count = 30, page = 1):
    """Get a user's channels"""
    uri = 'users/' + user_id + '/channels'
    options = {}
    return self.make_request(uri, options)

  def get_user_followers(self, user_id, count = 30, page = 1):
    """Get a user's followers"""
    uri = 'users/' + user_id + '/followers'
    options = { 'per_page': count, 'page': page}
    return self.make_request(uri, options)

  def get_user_following(self, user_id, count = 30, page = 1):
    """Get the users someone is following"""
    uri = 'users/' + user_id + '/following'
    options = { 'per_page': cont, 'page': page }
    return self.make_request(uri, options)

  def get_videos(self, count = 30, page = 1):
    """Get all videos"""
    uri = 'videos'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_sponsored_videos(self, count = 30, page = 1):
    """Get all sponsored videos"""
    uri = 'videos/sponsored'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_featured_videos(self, count = 30, page = 1):
    """Get all featured videos"""
    uri = 'videos/featured'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_latest_videos(self, count = 30, page = 1):
    """Get all videos sorted by recently added"""
    uri = 'videos/latest'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_vr_videos(self, count = 30, page = 1):
    """Get all videos marked as being VR optimized"""
    uri = 'videos/vr'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_video(self, video_id):
    """Get a video by its id or slug"""
    uri = 'videos/' + video_id
    return self.make_request(uri)

  # star_video

  # unstar_video

  def get_video_comments(self, video_id, count = 30, page = 1):
    """Get a video's comments"""
    uri = 'videos/' + video_id + '/comments'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  # add_video_comment

  def get_photos(self, count = 30, page = 1):
    """Get all photos"""
    uri = 'photos'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_featured_photos(self, count = 30, page = 1):
    """Get all featured photos"""
    uri = 'photos/featured'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_latest_photos(self, count = 30, page = 1):
    """Get all photos sorted by recently added"""
    uri = 'photos/latest'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_vr_photos(self, count = 30, page = 1):
    """Get all photos marked as VR optimized"""
    uri = 'photos/vr'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_photo(self, photo_id):
    """Get a photo by its id or slug"""
    uri = 'photos/' + photo_id
    return self.make_request(uri)

  # star photo

  # unstar photo

  def get_photo_comments(self, photo_id, count = 30, page = 1):
    """Get a photo's comments"""
    uri = 'photos/' + photo_id + '/comments'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_categories(count = 30, page = 1):
    """Get all categories"""
    uri = 'categories'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_category_info(category_id):
    """Get the metadata info for a category by its id"""
    uri = 'categories/' + category_id
    return self.make_request(uri)

  def get_videos_by_category(self, category_id, count = 30, page = 1):
    """Get all videos in a certain category"""
    uri = 'categories/' + category + '/videos'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_photos_by_category(self, category_id, count = 30, page = 1):
    """Get all photos in a certain category"""
    uri = 'categories/' + category_id + '/photos'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_channels(self, count = 30, page = 1):
    """Get all channels"""
    uri = 'channels'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_channel(self, channel_id):
    """Get a channel by its id"""
    uri = 'channels/' + channel_id
    return self.make_request(uri)

  def get_channel_videos(self, channel_id, count = 30, page = 1):
    """Get all the videos in a specific channel"""
    uri = 'channels/' + channel_id + '/videos'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_channel_photos(self, channel_id, count = 30, page = 1):
    """Get all the photos in a specific channel"""
    uri = 'channels/' + channel_id + '/photos'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_hashtags(self, count = 30, page = 1):
    """Get all hashtags"""
    uri = 'hashtags'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_hashtag_info(self, hashtag):
    """Get the metadata information about a hashtag"""
    uri = 'hashtags/' + hashtag
    return self.make_request(uri)

  def get_videos_by_hashtag(self, hashtag, count = 30, page = 1):
    """Get all the videos associated with a specific hashtag"""
    uri = 'hashtags/' + hashtag + '/videos'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def get_photos_by_hashtag(self, hashtag, count = 30, page = 1):
    """Get all photos associated with a specific hashtag"""
    uri = 'hashtags/' + hashtag + '/photos'
    options = { 'per_page': count, 'page': page }
    return self.make_request(uri, options)

  def make_request(self, uri, options = {}):
    querystring = ''
    if (len(options) > 0): querystring += '?' + urllib.urlencode(options)
    url = self.BASE_URL + uri + querystring
    headers = {
      'X-Apikey': self.apikey,
      'User-Agent': 'littlstar-python',
      'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    return response.json()
