# Adding Posts
## Open shell
```bash
python manage.py shell
```

## Add Post
```
from author.models import *
from blog.models import *
blog = Blog.query.first()
author = Author.query.first()
category = Category.query.first()
post = Post(blog, author, 'Python is cool!', 'This is why Python is cool.', category)
db.session.add(post)
db.session.commit()
```
