from rest_framework.response import Response


class APIResponse:
    """
    Unified API response contract
    """

    @staticmethod
    def success(data=None, meta=None, code=200):
        return Response(
            {
                "status": "success",
                "code": code,
                "data": data,
                "meta": meta or {}
            },
            status=code
        )

    @staticmethod
    def error(message="Error", errors=None, code=400):
        return Response(
            {
                "status": "error",
                "code": code,
                "message": message,
                "errors": errors or {}
            },
            status=code
        )