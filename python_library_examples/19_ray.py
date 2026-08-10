import ray

ray.init(ignore_reinit_error=True)

@ray.remote
def square(x):
    return x * x

print(ray.get([square.remote(i) for i in range(5)]))
