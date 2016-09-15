from rest_framework import permissions

class IsAuthenticatedOrCreate(permissions.IsAuthenticated):
  def has_permission(self, request, view):
    if request.method == 'POST':
      return True
    return super(IsAuthenticatedOrCreate, self).has_permission(request, view)

class IsOwnerOrReadOnly(permissions.BasePermission):
  """
  Custom permission to only allow owners of an object to edit it.
  """

  def has_object_permission(self, request, view, obj):
    # Read permissions are allowed to any request,
    # so we'll always allow GET, HEAD or OPTIONS requests.
    if request.method in permissions.SAFE_METHODS:
        return True

    # Write permissions are only allowed to the owner of the snippet.

    # IMPORTANT: In your object model, remember to have the field of 'owner'. If not, this is going to fail
    # Example of what you should have in your model: owner = models.ForeignKey('auth.User', related_name='something')
    # Check out the model Item
    return obj.owner == request.user