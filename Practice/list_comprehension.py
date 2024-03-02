import logger

log = logger.get_logger(__name__)

print(log)

x = [i for i in range(1,101)]
print(x)

x = [i for i in range(1,101) if i%3 != 0]
print(x)

x = [0 if i%2 ==0 else 1 for i in range (100)]
print(x)

