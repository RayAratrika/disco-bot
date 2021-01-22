import discord as dc;
import json;
import keys;
import last_fm as lfm;

token = keys.bot_token();

#need intents for accessing members and certain other details
bot = dc.Client(intents = dc.Intents.all());

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
				name="d-help",
				value="Info about the bot",
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
			bot_color = botsent.author.roles[-1].color.split('#')[1];
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
	
	og_msg = msg.content.lower();
	#disco-hello: greeting message
	if og_msg == ('d-hello'):
		dsc = "Hello "+ msg.author.mention +" my musical human fren :)"
		emb = dc.Embed(
			title = "Greetings!", 
			description = dsc, 
			color = bot_color); #liked- 3D5AFE, B39DDB, 90CAF9, 1123A0

		botsent = await msg.channel.send(embed = emb);
		await botsent.add_reaction('\N{VICTORY HAND}');
		bot_color = botsent.author.roles[-1].color;
		print(bot_color);		
		
	#disco-charts: chart hits top10 using threads
	elif og_msg == ('dt-charts'):
		i = 0; dsc = "";
		texts = lfm.chart_t();
		if texts == []:
			emb = dc.Embed(
				title = "OOPS!!", 
				description = "Try Again :(",
				color = bot_color);
		else:
			for t in texts:
				i += 1;
				dsc += str(i) + ". " + t;
				emb = dc.Embed(
					title = "Chart-Busters!!!", 
					description = "Here are some YouTube links for you: \n"+dsc,
					color = bot_color);

		botsent = await msg.channel.send(embed = emb);
		await botsent.add_reaction('\N{PENSIVE FACE}') if texts == [] else await botsent.add_reaction('\N{MUSICAL NOTE}');
		bot_color = botsent.author.roles[-1].color;
		
	#disco-artist-abc: top10 tracks of artists using threads
	elif og_msg.startswith('dta-'):
		artist = og_msg.split('dta-')[1];
		i = 0; dsc = "";
		texts = lfm.artist_t(artist);
		if texts == []:
			emb = dc.Embed(
				title = "OOPS!!", 
				description = "Couldn't find the artist you're looking for :(",
				color = bot_color);

		else: 
			for txt in texts:
				i += 1;
				dsc += str(i) + ". " + txt;
				emb = dc.Embed(
					title = "Top Tracks of "+ artist +"!", 
					description = "Here are some YouTube links for you: \n"+dsc,
					color = bot_color);

		botsent = await msg.channel.send(embed = emb);
		await botsent.add_reaction('\N{PENSIVE FACE}') if texts == [] else await botsent.add_reaction('\N{MUSICAL NOTE}');
		bot_color = botsent.author.roles[-1].color;
	

	#disco-charts: chart hits top10
	elif og_msg == ('d-charts'):
		i = 0; dsc = "";
		texts = lfm.chart();
		if texts == []:
			emb = dc.Embed(
				title = "OOPS!!", 
				description = "Try Again :(",
				color = bot_color);
		else:
			for t in texts:
				i += 1;
				dsc += str(i) + ". " + t;
				emb = dc.Embed(
					title = "Chart-Busters!!!", 
					description = "Here are some YouTube links for you: \n"+dsc,
					color = bot_color);

		botsent = await msg.channel.send(embed = emb);
		await botsent.add_reaction('\N{PENSIVE FACE}') if texts == [] else await botsent.add_reaction('\N{MUSICAL NOTE}');
		bot_color = botsent.author.roles[-1].color;

	#disco-artist-abc: top10 tracks of artists
	elif og_msg.startswith('da-'):
		artist = og_msg.split('da-')[1];
		i = 0; dsc = "";
		texts = lfm.artist(artist);
		if texts == []:
			emb = dc.Embed(
				title = "OOPS!!", 
				description = "Couldn't find the artist you're looking for :(",
				color = bot_color);

		else: 
			for txt in texts:
				i += 1;
				dsc += str(i) + ". " + txt;
				emb = dc.Embed(
					title = "Top Tracks of "+ artist +"!", 
					description = "Here are some YouTube links for you: \n"+dsc,
					color = bot_color);

		botsent = await msg.channel.send(embed = emb);
		await botsent.add_reaction('\N{PENSIVE FACE}') if texts == [] else await botsent.add_reaction('\N{MUSICAL NOTE}');
		bot_color = botsent.author.roles[-1].color;

	#disco-genre-abc: yt playlist links of genre
	elif og_msg.startswith('dg-'):
		genre = og_msg.split('dg-')[1];
		i = 0; dsc = "";
		texts = lfm.genre(genre);
		if texts == []:
			emb = dc.Embed(
				title = "OOPS!!", 
				description = "Couldn't find the genre you're looking for :(",
				color = bot_color);
		else:
			for txt in texts:
				i += 1;
				dsc += str(i) + ". " + txt;
				emb = dc.Embed(
					title = "Genre-ous", 
					description = "Here are some YouTube links for you: \n"+dsc,
					color = bot_color);

		botsent = await msg.channel.send(embed = emb);
		await botsent.add_reaction('\N{PENSIVE FACE}') if texts == [] else await botsent.add_reaction('\N{MUSICAL NOTE}');
		bot_color = botsent.author.roles[-1].color;
	
	#disco-info: info about the bot
	elif og_msg == ('d-help'):
		emb = dc.Embed(
			title = "Here is some helpful information about me-",
			color = bot_color);
		emb.add_field(
			name="d-hello",
			value="Greeting message",
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
			description = f"Yes {msg.author.mention} how can I be of help to you?\n\nTry out these commands-\n>> d-hello\n>> d-help\n>> d-charts\n>> dg-<genre>\n>> da-<artist>", 
			color = bot_color);

		botsent = await msg.channel.send(embed = emb);
		bot_color = botsent.author.roles[-1].color;
		await botsent.add_reaction('\N{EYES}');


bot.run(token);
