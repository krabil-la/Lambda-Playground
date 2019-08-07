import json
import base64


LYRICS = '''Yeah, I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more
I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more

I got the horses in the back
Horse tack is attached
Hat is matte black
Got the boots that's black to match
Ridin' on a horse, ha
You can whip your Porsche
I been in the valley
You ain't been up off that porch, now

Can't nobody tell me nothin'
You can't tell me nothin'
Can't nobody tell me nothin'
You can't tell me nothin'

Ridin' on a tractor
Lean all in my bladder
Cheated on my baby
You can go and ask her
My life is a movie
Bull ridin' and boobies
Cowboy hat from Gucci
Wrangler on my booty

Can't nobody tell me nothin'
You can't tell me nothin'
Can't nobody tell me nothin'
You can't tell me nothin'

Yeah, I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more
I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more

Hat down, cross town, livin' like a rockstar
Spent a lot of money on my brand new guitar
Baby's got a habit: diamond rings and Fendi sports bras
Ridin' down Rodeo in my Maserati sports car
Got no stress, I've been through all that
I'm like a Marlboro Man so I kick on back
Wish I could roll on back to that old town road
I wanna ride 'til I can't no more

Yeah, I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more
I'm gonna take my horse to the old town road
I'm gonna ride 'til I can't no more'''

# Additional steps
# https://stackoverflow.com/questions/35804042/aws-api-gateway-and-lambda-to-return-image

def lambda_handler(event, context):
    # TODO implement
    # return {'statusCode': 200,
    #         'body': LYRICS
    #     }

    with open("cage.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return {"isBase64Encoded": True,
      "statusCode": 200,
      "headers": { "content-type": "image/jpg"},
      "body":  encoded_string.decode("utf-8")
    }
