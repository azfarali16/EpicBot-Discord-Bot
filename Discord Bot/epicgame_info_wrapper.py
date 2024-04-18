
import discord

NA_IMAGE_URL = 'https://salonlfc.com/wp-content/uploads/2018/01/image-not-found-1-scaled.png'

PRODUCT_URL = 'https://store.epicgames.com/en-US/p/'

class GameInfoWrapper:
    def __init__(self, element):
        self.title = element['title']
        self.description = element['description']
        self.offer_type = element['offerType']
        self.seller_name = element['seller']['name']
        
        self.thumbnail_img = NA_IMAGE_URL
        self.key_img = NA_IMAGE_URL

        for image in element['keyImages']:
            if image['type'] == 'Thumbnail':
                self.thumbnail_img = image['url']
            elif image['type'] == 'OfferImageWide':
                self.key_img = image['url']
        

        self.page_url = PRODUCT_URL+element['catalogNs']['mappings'][0]['pageSlug']

        self.price = element['price']['totalPrice']['originalPrice']/100
        self.end_date = element['promotions']['promotionalOffers'][0]["promotionalOffers"][0]["endDate"][:10]

    def print_info(self):
        print("Title:", self.title)
        print("Description:", self.description)
        print("Offer Type:", self.offer_type)
        print("Seller Name:", self.seller_name)
        print("Price:", self.price)
        print("End Date:", self.end_date)
        print("______________________________")
        print("Thumbnail Image:", self.thumbnail_img)
        print("Key Image:",self.key_img)        
        print("______________________________")


    def game_info(self):
        game_info_template = """
Title: {title}
Description: {description}
Offer Type: {offer_type}
Seller Name: {seller_name}
Price: {price} $
End Date: {end_date}
        """

        msg = game_info_template.format(
            title=self.title,
            description=self.description,
            offer_type=self.offer_type,
            seller_name=self.seller_name,
            price=self.price,
            end_date=self.end_date,
        )
    
        return msg
    


    def game_info_embed(self):
        embed = discord.Embed(
            color = discord.Color.orange(),
            title=self.title,
            description=self.description,
            url = self.page_url
        )

        embed.set_author(name = self.seller_name)

        embed.set_thumbnail(url=self.thumbnail_img)
        embed.set_image(url=self.key_img)

        embed.set_footer(text = "Original Price: "+str(self.price))

        embed.add_field(name='Click to view the browser link!', value=f"[Click here!]({self.page_url})", inline=False)

        return embed


