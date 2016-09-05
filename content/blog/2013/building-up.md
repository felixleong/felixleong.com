title: Building Up
tags: technical, tech, python, work, career, life, talks
date: 2013-08-16T01:48:42Z
category: Programming
featured_image: http://farm6.staticflickr.com/5100/5472660657_666ace48a6.jpg
featured_image_credit: 'Seedling' by _sjg_, on Flickr
featured_image_url: http://www.flickr.com/photos/_sjg_/5472660657/

My journey in [Mindvalley](http://mindvalley.com/) is definitely an interesting one. When I first joined the company, I've been working on [CustomerHugs](http://customerhugs.com/) -- which is a web service for users to collect reviews and testimonials from Facebook users.

Unfortunately it is a service that didn't caught on and was now being in hibernation mode and isn't actively being supported at the moment[^1]. So in October last year, I was being assigned to my second solo project.

# The Second Act

The original idea is to come up with a supplementary API service that complements with [UrbanAirship](http://urbanairship.com/)'s in-app purchase service -- to be more specific about it, I'm assigned to come up with an API service that would provide just enough tools to create a more flexible in-app purchase store front for mobile apps, while leaving the content delivery and transaction tracking to UrbanAirship.

It was supposed to be a small project -- fixing a small pain point and move on to any future project that would come my way in two months. Little did I know is that as months goes by, this small project have become a full stack solution in handling in-app purchases for iOS (and we ended up not using UrbanAirship at all -- which they discontinued the in-app purchase service later this year).

Ever since it is live on February with the launch of [Omvana](http://omvana.com/), it has been a very treacherous and rewarding adventure. Having to race against time to learn as much as I could, slaying all the mysterious bugs that plagues the service as well as dealing with the stress of receiving an SMS saying that the server is overloaded and cannot handle all the traffic we are getting.

![CPU usage chart - before and after panic period]({static}/images/2013/cpu-month.png){: .img-responsive}

The part about receiving SMSes proves to be quite a stress tumour, in fact. It started off pretty benign -- the downtime would probably just last about three minutes and everything would work like magic again after that. As we start to gain traction and our marketing efforts for Omvana becoming more successful over time, the downtimes would occur several times in a day with each downtime lasts for at least 15-20 minutes.

I'm really fortunate that I'm able to work with [Gareth Davies](http://shaolintiger.com/) -- who helped immensely in switching our monolithic setup to a horizontally-scalable setup _(read: running across several servers)_. And ever since early August, all the stressful SMS that lasted for months has finally stopped.

Looking back now, here are the full list of things that I've learned so far during my development life in Mindvalley:

- Learned Django, its internals and a growing number of useful libraries
- [REST API](http://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) design and best practices
- Improved my tool set and development environment for Python
- Unit testing, gone are the days of cowboy programming
- Dealing with database migrations and all the incompatibilities and nuances _(and figured that I don't like MySQL as much as I used to and prefering PostgreSQL)_
- Managing project time lines and feature priorities _(proves to be even more important because I'm managing myself as a solo developer)_
- Planning for horizontal scaling and infrastructure changes _(though Gareth most of the heavylifting in terms of actually configuring stuff)_
- Performance tuning and monitoring
- Using asynchronous task queues and getting bit by all the pitfalls that comes with it

Granted, as the project continues to grow, the bugs are starting to become gnarled and harder to slay and there's __WAAAAY__ more improvements that needs to be included. This shows how much more I can learn from this project and I'm more than happy to grow together with it. :)

## Contributing Back

Having gone through an intense year of development, I'm now much more comfortable to share the knowledge that I've learned so far. Granted that I still have a lot of learn and I'm nowhere from attaining guru status. But the least I can contribute back is to share my learnings from a novice's perspective and hopefully it'd help someone :).

I really look up to [LincolnLoop](http://lincolnloop.com/blog/) and would think of them as my role model in this journey.

In fact, to start things off, [I have given a talk titled "REST API 101" at Webcamp KL](https://github.com/felixleong/wckl_restapi_talk) -- which serves as a primer to REST API. And this month I'll be doing another talk at [Webcamp KL](http://facebook.com/groups/webcamp/) on my experience in horizontally scaling my API web service.

And in terms of open source contributions, I've just recently push a fork to [django-tastypie-extendedmodelresource](https://github.com/felixleong/django-tastypie-extendedmodelresource/tree/develop) -- a convenience library to create nested resources using Django-Tastypie _(e.g. creating API endpoints that looks like /api/v1/authors/cslewis/books/)_.

Other than that, am really looking forward to all the things I'll be able to learn in months to come! :)

[^1]: For the record it's still working and you can still sign up for a new account, but paying for zero support is something I won't vouch for. :p
