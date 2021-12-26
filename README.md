![](https://graphics.thomsonreuters.com/style-assets/images/logos/reuters-graphics-logo/svg/graphics-logo-color-dark.svg)

# django-graphics_token

Models for creating and managing Django Rest Framework API tokens, authentication and permissions.

## Quickstart

1. Install the app from GitHub:

   ```bash
   pipenv install -e git+https://github.com/reuters-graphics/django-graphics-token.git#egg=django-graphics_token
   ```

2. Add "graphics_token" to your INSTALLED_APPS setting like this:

   ```python
   INSTALLED_APPS = [
       # ...
       "rest_framework",
       "graphics_token",
   ]
   ```

3. Include the graphics_token URLconf in your project's `urls.py` like this:

   ```python
   from django.urls import include, path

   urlpatterns = [
      # ...
      path("graphics-token/", include("graphics_token.urls")),
   ]
   ```

4. Run `python manage.py migrate` to create graphics_token models.

5. Create a token user in the graphics_token admin and use the generated token to authenticate your fetch requests like this (Note the format of the Authorization header, "Token" + whitespace + your token):

   ```javascript
   fetch("https://yourapp.com/your/api/endpoint/", {
     method: "GET",
     headers: {
       Authorization: `Token ${YOUR_APP_TOKEN_HERE}`,
       "Content-Type": "application/json",
     },
   })
     .then((response) => response.json())
     .then((data) => {
       console.log(data);
     });
   ```

## Authentication/Permissions

You can use built-in classes to authenticate and permission your requests. Permissioning uses Django's native permission model to validate requests based on model permissions.

```python
from myapp.models import MyModel
from myapp.serializers import MyModelSerializer
from rest_framework.viewsets import ModelViewSet

from graphics_token.authentication import TokenAuthentication
from graphics_token.permissions import TokenModelPermissions


class MyModelViewSet(ModelViewSet):
    serializer_class = MyModelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (TokenModelPermissions,)
    queryset = MyModel.objects.all()
```

## Developing

Read more about developing this app in the [Developing](./DEVELOPING.md) docs.
