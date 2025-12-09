# Infinite iterator (Careful!)
class Infinite:
    def _iter_ (self):
        self.x = 1
        return self
    def _next_ (self):
        self.x += 1
        return self.x 
    
it = Infinite()

print(next(it))
print(next(it))

