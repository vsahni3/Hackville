import cohere

co = cohere.Client('ZG1hp4UsOagPS7V8vOiSxkGMljolDMPi96KAvboq')

def reply(prompt):

    response = co.generate(
    model='command-xlarge-nightly',
    prompt=prompt,
    max_tokens=150,
    temperature=0.8,
    stop_sequences=["--"],
    return_likelihoods='NONE',
    truncate='START')
    return response.generations[0].text

prompt1a = f"""
I am 71 years old. I will add my comfort levels as a number on a scale from 1-10, with using the 
following fields below:
Banking: 1
Hardware: 4
Social Media: 2
Here is some additional info about how comfortable I am with using technology:
I struggle with navigating social media websites like Facebook and YouTube.
Specifically with uploading pictures to social media.

Based on the scores and the additional information provided, respond to the following question to help with technology.
How do I send a friend request on Facebook?

Response: 
Here are the steps to send a friend request on Facebook:

1. Log in to your Facebook account.
2. Click on the "Friends" tab at the top of the page.
3. Click on the "Add Friends" button.
4. Enter the name or email of the person you want to add as a friend.
5. Click on the "Send Friend Request" button.

You will receive a notification when your friend request is accepted.

"""
print(reply(prompt1a))

prompt1b = f"""
I am 71 years old. I will add my comfort levels as a number on a scale from 1-10, with using the 
following fields below:
Banking: 1
Hardware: 4
Social Media: 2
Here is some additional info about how comfortable I am with using technology:
I struggle with navigating social media websites like Facebook and YouTube.
Specifically with uploading pictures to social media.

Based on the scores and the additional information provided, respond to the following question to help with technology asked by the above user.
Step by step instructions on how to make a payment online.

Response: Here are some step-by-step instructions on how to make a payment online:
1. Go to your bank's website and log in to your account.
2. Click on the "Payments" or "Bill Pay" tab.
3. Enter the name of the company or person you want to pay, the amount you want to pay, and the payment date.
4. Select the payment method you want to use. You can choose to pay with a debit card
"""

print(reply(prompt1b))

prompt1c = f"""
I am 71 years old. I will add my comfort levels as a number on a scale from 1-10, with using the 
following fields below:
Banking: 1
Hardware: 4
Social Media: 2
Here is some additional info about how comfortable I am with using technology:
I struggle with navigating social media websites like Facebook and YouTube.
Specifically with uploading pictures to social media.

Based on the scores and the additional information provided, respond to the following question to help with technology asked by the above user.
Step by step instructions on how to send an e-transfer.

Response:
Here are step-by-step instructions on how to send an e-transfer:
1. Open the E-transfer website or app on your device.
2. Enter the recipient's email address or phone number and the amount you want to send.
3. Choose a security question and answer.
4. Review the payment details and click "Confirm" to submit the payment.
5. Click or tap the "Confirm" button.
That's it! The funds will be sent to the recipient's account.
I hope these instructions help!
"""

print(reply(prompt1c))

prompt1d = f"""
I am 71 years old. I will add my comfort levels as a number on a scale from 1-10, with using the 
following fields below:
Banking: 1
Hardware: 4
Social Media: 2
Here is some additional info about how comfortable I am with using technology:
I struggle with navigating social media websites like Facebook and YouTube.
Specifically with uploading pictures to social media.

Based on the scores and the additional information provided, respond to the following question to help with technology asked by the above user.
Step by step instructions on how to save a photo I like from facebook onto my phone.

Response:
Here are step-by-step instructions on how to save a photo you like from Facebook onto your phone:
1. Open the Facebook app on your phone and log in to your account.
2. Find the photo you want to save and tap on it to open it.
3. Tap on the three dots in the top right corner of the photo and select Save Photo from the menu that appears.
4. The photo will be saved to your phone's gallery.
"""

print(reply(prompt1d))

prompt2a = f"""
I am 65 years old. I will add my comfort levels as a number on a scale from 1-10, using the 
following fields below:
Banking: 1
Hardware: 4
Social Media: 4

Here is some additional info about how comfortable I am with using technology:
I struggle with understanding how to fix my Internet connection
I dont understand why it is important to do a software update on my computer

Based on the scores and the additional information provided, respond to the following question to help with technology.
Step by step instructions on how to resolve issues with connecting to a Wi-Fi network?

Response:
Here are some step-by-step instructions on how to resolve issues with connecting to a Wi-Fi network:
Check that the Wi-Fi network is turned on and that the device is within range of the network.
Verify that the network name and password are correct.
Try restarting the device.
""" 

print(reply(prompt2a))


prompt2b = f"""
I am 65 years old. I will add my comfort levels as a number on a scale from 1-10, using the 
following fields below:
Banking: 1
Hardware: 4
Social Media: 4

Here is some additional info about how comfortable I am with using technology:
I struggle with understanding how to fix my Internet connection
I dont understand why it is important to do a software update on my computer

Based on the scores and the additional information provided, respond to the following question to help this user with technology.
Step by step instructions on how to install a new app on my smartphone?

Response:
Here are some step-by-step instructions on how to install a new app on a smartphone:

1. Open the App Store or Google Play on your phone.
2. Search for the app you want to install.
3. Tap on the app you want to install.
4. Tap on the "Install" button.
5. Enter your password if prompted.
6. The app will begin installing."
"""

print(reply(prompt2b))

prompt2c = f"""
I am 65 years old. I will add my comfort levels as a number on a scale from 1-10, using the 
following fields below:
Banking: 1
Hardware: 4
Social Media: 4

Here is some additional info about how comfortable I am with using technology:
I struggle with understanding how to fix my Internet connection
I dont understand why it is important to do a software update on my computer

Based on the scores and the additional information provided, respond to the following question to help this user with technology.
Why cant I take anymore pictures on my phone even though I've deleted two apps? It keeps saying that there is no storage left on my device.

Response:
It sounds like you are having trouble with your phone's storage. Have you tried deleting any apps or files that you no longer need? You can also try moving any photos or videos you have saved to your computer or another storage device. This should free up some space on your phone and allow you to take more pictures.
"""
print(reply(prompt2c))

prompt2d = f"""
I am 65 years old. I will add my comfort levels as a number on a scale from 1-10, using the 
following fields below:
Banking: 1
Hardware: 4
Social Media: 4

Here is some additional info about how comfortable I am with using technology:
I struggle with understanding how to fix my Internet connection.
I dont understand why it is important to do a software update on my computer.

Based on the scores and the additional information provided, respond to the following question to help this user with technology.
How do I enable voice control like siri to be able to send text messages to my grandson while im in the car?

Response:
You can enable Siri on your iPhone to send text messages to your grandson while you are in the car. To do this, go to Settings > Siri & Search and toggle on the Listen for "Hey Siri" option. Then, when you are in your car and want to send a message, simply say "Hey Siri" and give the command. For example, you could say "Hey Siri, send a text message to my grandson."

"""

print(reply(prompt2d))

prompt3a = f"""
I am 60 years old. I will add my comfort levels as a number on a scale from 1-10, using the 
following fields below:
Banking: 10
Hardware: 3
Social Media: 10

Here is some additional info about how comfortable I am with using technology:
I am very good with understaning the banking apps and comfortable with using social media
I struggle with understanding which wires are needed for my TV to work

Based on the scores and the additional information provided, respond to the following question to help with technology.
Which wires are needed to connect my computer to a monitor?

Response:
The wires needed to connect a computer to a monitor are typically included with the monitor. These wires may include a power cable, a video cable, and possibly a sound cable. The specific types of cables needed may vary depending on the model of monitor and computer being used.
To connect the monitor to the computer, first identify the ports on the back of the monitor and the computer. The ports on the monitor may be labeled with letters or symbols, such as "VGA," "HDMI.
Older Apple devices used a 30-pin dock connector, while newer devices use a Lightning connector.
"""

print(reply(prompt3a))

prompt3b = f"""
I am 60 years old. I will add my comfort levels as a number on a scale from 1-10, using the 
following fields below:
Banking: 10
Hardware: 3
Social Media: 10

Here is some additional info about how comfortable I am with using technology:
I am very good with understaning the banking apps and comfortable with using social media
I struggle with understanding which wires are needed for my TV to work

Based on the scores and the additional information provided, respond to the following question to help with technology.
Why doesnt my old iphone charger connect to my new macbook?

Response:
The iphone charger is a lightning connector and the macbook uses a USB-C connector.
Both the iphone charger and the macbook charger use different connectors, so the iphone charger will not be able to connect to the macbook.
"""

print(reply(prompt3b))

prompt3c = f"""
I am 60 years old. I will add my comfort levels as a number on a scale from 1-10, using the 
following fields below:
Banking: 10
Hardware: 3
Social Media: 10

Here is some additional info about how comfortable I am with using technology:
I am very good with understaning the banking apps and comfortable with using social media
I struggle with understanding which wires are needed for my TV to work

Based on the scores and the additional information provided, respond to the following question to help with technology.
How do I delete the "other" storage from my iphone?

Response:
To delete the "other" storage from your iPhone, you will need to go into your settings and find the storage section. Once you are in the storage section, you should see a list of all of the storage on your phone, including the "other" storage. Click on the "other" storage and you should see a button that says "delete." Click on that button and the "other" storage will be deleted from your phone.
"""

print(reply(prompt3c))

prompt3d = f"""
I am 60 years old. I will add my comfort levels as a number on a scale from 1-10, using the 
following fields below:
Banking: 10
Hardware: 3
Social Media: 10

Here is some additional info about how comfortable I am with using technology:
I am very good with understaning the banking apps and comfortable with using social media
I struggle with understanding which wires are needed for my TV to work

Based on the scores and the additional information provided, respond to the following question to help with technology.
Can I see who recently visited my Facebook page? Or can users see that Ive vistied their Facebook page?

Response:
Since you said you are comfortable with using social media apps, it is possible for you to see who has recently visited your Facebook page. However, it is not possible for users to see that you have visited their Facebook page.
"""

print(reply(prompt3d))