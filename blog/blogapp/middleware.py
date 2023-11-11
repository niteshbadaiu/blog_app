def blog_middleware(get_response):
    print("code to execute for intialization only once")

    def my_middleware(request):
        print("code executed before view function is called")
        res=get_response(request)
        print(res)
        print("code executed after view function is called")
        return res
    
    return my_middleware