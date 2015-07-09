#Littlstar Python SDK
This SDK is a Python wrapper class around the Littlstar api (http://developer.littlstar.com/docs/), and allows you to access all our content with convenient methods.

##Example
```python
import littlstarsdk

api_key = 'your-api-key'

ls = littlstar.SDK(api_key)

videos = ls.get_videos()
```

##Methods Implemented

####search
Search Littlstar for photos, videos, users, or everything.  
```endpoint``` [all|users|photos|videos]  
```query``` the search term  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
search(endpoint, query, count = 30, page = 1)
```

####get_user
Get a user by id or slug.  
```user_id``` The user's unique id or slug  
```python
get_user(user_id)
```

####get_user_videos
Get a user's videos.  
```user_id``` the user's unique id or slug  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_user_videos(user_id, count = 30, page = 1)
```

####get_user_photos
Get a user's photos.  
```user_id``` the user's unique id or slug  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_user_photos(user_id, count = 30, page = 1)
```

####get_user_channels
Get a user's channels.  
```user_id``` the user's unique id or slug  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_user_channels(user_id, count = 30, page = 1)
```

####get_user_followers
Get a user's followers.  
```user_id``` the user's unique id or slug  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_user_followers(user_id, count = 30, page = 1)
```

####get_user_following
Get the users someone is following.  
```user_id``` the user's unique id or slug  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_user_following(user_id, count = 30, page = 1)
```
####get_videos
Get all videos.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_videos(count = 30, page = 1)
```

####get_sponsored_videos
Get all sponsored videos.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_sponsored_videos(count = 30, page = 1)
```
####get_featured_videos
Get all featured videos.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_featured_videos(count = 30, page = 1)
```

####get_latest_videos
Get all videos sorted by recently added.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_latest_videos(count = 30, page = 1)
```

####get_vr_videos
Get all videos that have been marked as VR optimized.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_vr_videos(count = 30, page = 1)
```

####get_video
Get a video by its unique id or slug.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_video(video_id)
```

####get_video_comments
Get a video's comments.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_video_comments(video_id, count = 30, page = 1)
```

####get_photos
Get all photos.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_photos(count = 30, page = 1)
```

####get_featured_photos
Get all featured photos.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_featured_photos(count = 30, page = 1)
```

####get_latest_photos
Get all photos sorted by recently added.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_latest_photos(count = 30, page = 1)
```

####get_vr_photos
Get all photos marked as VR optimized.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_vr_photos(count = 30, page = 1)
```

####get_photo
Get a photo by its unique id or slug.  
```video_id``` max # of results to show (default: 30)  
```python
get_photo(video_id)
```

####get_photo_comments
Get a photo's comments.  
```photo_id``` the photo's unique id or slug  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_photo_comments(video_id)
```

####get_categories
Get all categories.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_categories(count = 30, page = 1)
```

####get_category_info
Get the metadata for a category.  
```category_id``` the category's unique id or slug  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_category_info(category_id, count = 30, page = 1)
```

####get_videos_by_category
Get all videos in a category.  
```category_id``` the category's unique id or slug  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_videos_by_category(category_id, count = 30, page = 1)
```

####get_photos_by_category
Get all photos in a category.  
```category_id``` the category's unique id or slug  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_photos_by_category(category_id, count = 30, page = 1)
```

####get_channels
Get all Littlstar channels.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_channels(count = 30, page = 1)
```

####get_channel
Get a channel by its unique id or slug.  

####get_channel_videos
Get all videos in a channel.  
```channel_id``` the channel's unique id or slug  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_channel_videos(channel_id, count = 30, page = 1)
```

####get_channel_photos
Get all photos in a channel.  
```channel_id``` the channel's unique id or slug  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_channel_photos(channel_id, count = 30, page = 1)
```

####get_hashtags
Get all hashtags.  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_hashtags(count = 30, page = 1)
```

####get_hashtag_info
Get the metadata information about a hashtag.  
```hashtag``` the hashtag to search for  
```python
get_hashtag_info(hashtag)
```

####get_videos_by_hashtag
Get all the videos associated with a specific hashtag.  
```hashtag``` the hashtag to search for  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_videos_by_hashtag(hashtag, count = 30, page = 1)
```

####get_photos_by_hashtag
```hashtag``` the hashtag to search for  
```count``` max # of results to show (default: 30)  
```page``` paginated results (default: 1)  
```python
get_photos_by_hashtag(hashtag, count = 30, page = 1)
```
