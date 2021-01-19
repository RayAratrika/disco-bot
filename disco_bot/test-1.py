import discord as dc;
import json;
import keys;
import last_fm as lfm;

token = keys.bot_token();

#need intents for accessing members and certain other details
bot = dc.Client(intents = dc.Intents.all());
bot_color = 0xFFA000;

#on server join
@bot.event
async def on_guild_join(guild):
	bot_color = 0xFFA000;
	for ch in guild.text_channels: 
		if ch.permissions_for(guild.me).send_messages: 
			emb = dc.Embed(
				title = "Hello!", 
				description = "Hi! I'm Disco, a music suggestion bot.\nLet's get ready for some music, shall we?\n\nAdd me to other servers with the link below:\nhttps://discord.com/api/oauth2/authorize?client_id=800048826756890655&permissions=3214400&scope=bot \nHere are some commands I follow:\n",
				color = bot_color);
			emb.add_field(
				name="d-hello",
				value="Greeting message",
				inline=True);
			emb.add_field(
				name="d-info",
				value="Info about the bot",
				inline=True);
			emb.add_field(
				name="d-h",
				value="Suggest happy songs",
				inline=True);
			emb.add_field(
				name="d-l",
				value="Suggest sad songs",
				inline=True);
			emb.add_field(
				name="da-<artist>",
				value="Suggest top 10 songs of the artist",
				inline=True);
			emb.add_field(
				name="dg-<genre>",
				value="Suggest 10 <genre> playlist",
				inline=True);

			botsent = await ch.send(embed = emb);
			bot_color = botsent.author.roles[-1].color;
		break;

#on bot ready
@bot.event
async def on_ready():
	print(f"{bot.user} ready...")

#on message on channel
@bot.event
async def on_message(msg):
	bot_color = 0xFFA000;
	# check if author is bot or not
	if msg.author == bot.user: return;

	#disco-hello: greeting message
	if msg.content == ('d-hello'):
		dsc = "Hello "+ msg.author.mention +" my musical human fren :)"
		emb = dc.Embed(
			title = "Greetings!", 
			description = dsc, 
			color = bot_color);#  liked- 3D5AFE, B39DDB, 90CAF9, 1123A0

		botsent = await msg.channel.send(embed = emb);
		bot_color = botsent.author.roles[-1].color;
		#for role in msg.guild.roles: print(role.name, ": ",role.color);
		#print(botsent.author.roles[-1].color);
		print(type(bot.user));

	#disco-h: happy songs
	elif msg.content == ('d-h'):
		emb = dc.Embed(
			title = "Happy Happy Happy!",
			description = "Here are some happy songs for you-\n1.Dancing with myself - Billy Idol\n2.Back in the game - Airbourne\n\nGlad I could take part in your happiness!",
			color = bot_color);

		await msg.channel.send(embed = emb);
	
	#disco-l: sad songs
	elif msg.content == ('d-l'):
		emb = dc.Embed(
			title = "Feeling Low?", 
			description = "Here are some low songs for you-\n1.Lovely - Billie Eilish ft. Khalid\n2.In loving memeory - Alter Bridge\n\nI'm here if you need me for anything my friend :)",
			color = bot_color);

		botsent = await msg.channel.send(embed = emb);
		bot_color = botsent.author.roles[-1].color;

	#disco-charts: chart hits top10
	elif msg.content == ('d-charts'):
		i = 0; dsc = "";
		texts = lfm.chart();
		for txt in texts:
			i += 1;
			dsc += str(i) + ". " + txt;
		emb = dc.Embed(
			title = "Chart-Busters!!!", 
			description = "Here are some YouTube links for you: \n"+dsc,
			color = bot_color);

		botsent = await msg.channel.send(embed = emb);
		bot_color = botsent.author.roles[-1].color;

	#disco-artist-abc: top10 tracks of artists
	elif msg.content.startswith('da-'):
		artist = msg.content.split('da-')[1];
		i = 0; dsc = "";
		texts = lfm.artist(artist);
		for txt in texts:
			i += 1;
			dsc += str(i) + ". " + txt;
		emb = dc.Embed(
			title = "Top Tracks of "+ artist +"!", 
			description = "Here are some YouTube links for you: \n"+dsc,
			color = bot_color);

		botsent = await msg.channel.send(embed = emb);
		bot_color = botsent.author.roles[-1].color;
	
	#disco-genre-abc: yt playlist links of genre
	elif msg.content.startswith('dg-'):
		genre = msg.content.split('dg-')[1];
		i = 0; dsc = "";
		texts = lfm.genre(genre);
		for txt in texts:
			i += 1;
			dsc += str(i) + ". " + txt;
		emb = dc.Embed(
			title = "Genre-ous", 
			description = "Here are some YouTube links for you: \n"+dsc,
			color = bot_color);

		botsent = await msg.channel.send(embed = emb);
		bot_color = botsent.author.roles[-1].color;
	
	#disco-info: info about the bot
	elif msg.content == ('d-help'):
		emb = dc.Embed(
			title = "Here is some helpful information about me-",
			color = bot_color);
		emb.add_field(
			name="d-hello",
			value="Greeting message",
			inline=True);
		emb.add_field(
			name="d-h",
			value="Suggest happy songs",
			inline=True);
		emb.add_field(
			name="d-l",
			value="Suggest sad songs",
			inline=True);
		emb.add_field(
			name="dg-<genre>",
			value="Suggest 10 <genre> playlist",
			inline=True);
		emb.add_field(
			name="da-<artist>",
			value="Suggest top 10 songs of <artist>",
			inline=True);
		emb.add_field(
			name="d-help",
			value="Info about the bot",
			inline=True);

		await msg.channel.send(embed = emb);
	
	#mentioning the bot
	if bot.user.mentioned_in(msg) and msg.mention_everyone is False:
		emb = dc.Embed(
			title = "I'm needed?!", 
			description = f"Yes {msg.author.mention} how can I be of help to you?\n\nTry out these commands-\n>>d-hello\n>> d-h\n>> d-l\n>> d-charts\n>> dg-<genre>\n>> da-<artist>\n>> d-info", 
			color = bot_color);

		botsent = await msg.channel.send(embed = emb);
		bot_color = botsent.author.roles[-1].color;
		await botsent.add_reaction("\N{EYES}");


bot.run(token);