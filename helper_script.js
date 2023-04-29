var m = `Twitter: twitter.com/username
Facebook: facebook.com/username
Instagram: instagram.com/username
LinkedIn: linkedin.com/in/username
GitHub: github.com/username
Reddit: reddit.com/user/username
YouTube: youtube.com/channel/username
YouTubeUser: youtube.com/user/username
Twitch: twitch.tv/username
TikTok: tiktok.com/@username
Pinterest: pinterest.com/username
SoundCloud: soundcloud.com/username
Vimeo: vimeo.com/username
Medium: medium.com/@username
Discord: discord.com/username#discriminator
Snapchat: snapchat.com/add/username
WhatsApp: wa.me/username
Skype: skype.com/username
Slack: yourworkspace.slack.com/team/username
Zoom: zoom.us/j/username
Microsoft Teams: teams.microsoft.com/l/persona/username
Google Meet: meet.google.com/username 
Yahoo! Mail: mail.yahoo.com/d/username
AOL Mail: mail.aol.com/username`;

m.split('\n').forEach(line => {
	var name = line.split(':')[0];
	var template = line.split(':')[1].trim();
	console.log('"'+name+';'+name.toLowerCase()+';'+template.replace('username', '<%un%>').replace('discriminator', '<%d%>')+'",')
})