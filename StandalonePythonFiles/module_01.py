# modules
import module 
print (module.doThis())
print (module.doThat(4))
also = module.alsoDoThis
print (also())
from module import evenDoThis
print(evenDoThis())
# builtins are pre-existing modules
import builtins
print ('\n\nbuilt in modules')
print (dir(builtins))
