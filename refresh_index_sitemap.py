#!/usr/bin/env python3
"""Add the batch D and E posts to the blog index and rebuild the sitemap from disk."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_new_content import update_blog_index, rebuild_sitemap
import new_posts_d, new_posts_e

posts = new_posts_d.POSTS + new_posts_e.POSTS
print("blog index: added", update_blog_index(posts), "cards")
print("sitemap:", rebuild_sitemap(posts), "URLs")
