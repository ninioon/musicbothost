const Discord = require('discord.py');
const client = new Discord.CLient();

client.on('ready', () => {
    console.log('I am ready!');
 });
 
 client.on('message', message => {
    if (message.content === 'ping') {
      message.reply('pong');
      }
});

//Must be this way
client.login(process.env.BOT_TOKEN)'
