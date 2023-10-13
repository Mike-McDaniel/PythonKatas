# safe vs spooky rating. Scale of 1-5. "safe" is a rating of 2 or less. "spooky" is a rating of 3 or more.
def is_spooky(rating):
    if rating >= 3:
        return "Spooky"
    else:
        return "Safe"
    
# def is_spooky(rating):
#     if rating == 5:
#         return "Too Spooky" 



    # def too_spooky(rating):
    # spooky = ()
    # if rating > 2:
    #     spooky = rating*2
    #     return spooky