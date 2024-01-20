import Solve

# Solve ReCaptcha
result = Solve.ReCaptcha(
    '6LfEaFkUAAAAAGnIJMG983t2JyYg0McK4CUuRAdk', # siteKey
    'https://www.up-4ever.net/' # URL Website
)
print(result)



# Solve HCaptcha
# result = Solve.HCaptcha(
#     '4c672d35-0701-42b2-88c3-78380b0db560', # siteKey
#     'https://discord.com/' # URL Website
# )
# print(result)
