from shop.api.v1.core.response import APIResponse


class BaseAPIViewMixin:
    """
    All API views must inherit this to enforce contract
    """

    def success(self, data=None, meta=None, code=200):
        return APIResponse.success(data=data, meta=meta, code=code)

    def error(self, message="Error", errors=None, code=400):
        return APIResponse.error(message=message, errors=errors, code=code)