from telethon import events
from userbot.utils import Xa_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd

PRINTABLE_ASCII = range(0x21, 0x7F)


def aesthetify(string):
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@Xa_cmd(pattern="ae(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    text = event.pattern_match.group(1)
    text = "".join(aesthetify(text))
    await event.edit(text=text, parse_mode=None, link_preview=False)
    raise events.StopPropagation


CMD_HELP.update({
    "aeshtetic":
    f"𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝`{cmd}ae <teks>`\
    \n⌬ Mengubah fonts teks"
})
