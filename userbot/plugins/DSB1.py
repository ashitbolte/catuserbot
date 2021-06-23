from userbot import catub
import asyncio
plugin_category = "Extra"

@catub.cat_cmd(
    pattern="ssa$",
    command=("ssa", plugin_category),
    info={
        "header": "Asks User For SS of About Phone",
        "usage": "{tr}ssa",
    },
)
async def _(event):
    await event.edit("Share a screenshot of About Phone Page.\n\n You Can Find it here **Settings > About phone > Android version**")


@catub.cat_cmd(
    pattern="ssm$",
    command=("ssm", plugin_category),
    info={
        "header": "Asks User For SS of their Magisk Modules",
        "usage": "{tr}ssm",
    },
)
async def _(event):
    await event.edit("Share **Screenshots** of Installed Magisk Modules from Magisk App Here.")


@catub.cat_cmd(
    pattern="cut$",
    command=("cut", plugin_category),
    info={
        "header": "Gives Instructions of How to Fix Cut Issue",
        "usage": "{tr}cut",
    },
)
async def _(event):
    await event.edit("That Can Be Fixed Very Easily By Changing Statusbar Height from : \n**Developer Settings > Display Cutout** \n\nNote: Some roms have this on **Settings > Display Settings**")



@catub.cat_cmd(
    pattern="edsb$",
    command=("edsb", plugin_category),
    info={
        "header": "Asks User For SS of their Magisk Modules",
        "usage": "{tr}edsb",
    },
)
async def _(event):
    await event.edit("**1.** Flash correct DSB module, left DSB will be activated automatically. (Keep clock on left side)\n\n**2.** For Right DSB set Network Traffic to Expanded Header ( or QS Header/Quick Statusbar)")
    


@catub.cat_cmd(
    pattern="uiq$",
    command=("uiq", plugin_category),
    info={
        "header": "Asks for SystemUI.apk on Android 10 ROMs",
        "usage": "{tr}uiq",
    },
)
async def _(event):
    await event.edit("Send me your **SystemUI.apk** in PM.\n\nFor **(A10)**, You'll find it here : ```root/system/product/priv-app/SystemUI/SystemUI.apk```\n\n(__Choose one of__ [these styles](https://t.me/dualstatusbar/74824) __if you want to__)")



@catub.cat_cmd(
    pattern="ui$",
    command=("ui", plugin_category),
    info={
        "header": "Asks for SystemUI.apk on Android 11 ROMs",
        "usage": "{tr}ui",
    },
)
async def _(event):
    await event.edit("Send me your **SystemUI.apk** in PM.\n\nFor **(A11)**, You'll find it here : ```root/system/system-ext/priv-app/SystemUI/SystemUI.apk```\n\n(__Choose one of__ [these styles](https://t.me/dualstatusbar/74824) __if you want to__)")




@catub.cat_cmd(
    pattern="sss$",
    command=("sss", plugin_category),
    info={
        "header": "Tells User About The 2 Styles of DSB.",
        "usage": "{tr}sss",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/dualstatusbar/74824) **to Check Differences and Screenshot of both Style 1 & 2. ** ")




@catub.cat_cmd(
    pattern="bf$",
    command=("bf", plugin_category),
    info={
        "header": "Tells User about How To delete Magisk Modules from Recovery.",
        "usage": "{tr}bf",
    },
)
async def _(event):
    await event.edit("Read Steps About **How To Delete A Magisk Module via Recovery**: [Click Here](http://telegra.ph/How-to-delete-a-Magisk-module-from-Recovery-06-06)\n\nThis is Useful When You Face Bootloop or Black Screen after Installing DSB.")





# POST LINKS TO EVERY ROM





@catub.cat_cmd(
    pattern="aex$",
    command=("aex", plugin_category),
    info={
        "header": "AEX/CAFEX Post Link",
        "usage": "{tr}aex",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1373) to access **AEX/CAFEX** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="ascen$",
    command=("ascen", plugin_category),
    info={
        "header": "Ascendant/Descendant Post Link",
        "usage": "{tr}ascen",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1375) to access **AscendantOS/DescendantOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="arrow$",
    command=("arrow", plugin_category),
    info={
        "header": "ArrowOS Post Link",
        "usage": "{tr}arrow",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1284) to access **ArrowOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="cherish$",
    command=("cherish", plugin_category),
    info={
        "header": "CherishOS Post Link",
        "usage": "{tr}cherish",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1305) to access **CherishOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="corvus$",
    command=("corvus", plugin_category),
    info={
        "header": "CorvusOS Post Link",
        "usage": "{tr}corvus",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1303) to access **CorvusOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="crdroid$",
    command=("crdroid", plugin_category),
    info={
        "header": "CrDroid Post Link",
        "usage": "{tr}crdroid",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1317) to access **CrDroid** DSBs for all ROM versions.")





@catub.cat_cmd(
    pattern="desc$",
    command=("desc", plugin_category),
    info={
        "header": "Ascendant/Descendant Post Link",
        "usage": "{tr}desc",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1375) to access **AscendantOS/DescendantOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="derp$",
    command=("derp", plugin_category),
    info={
        "header": "Derpfest Post Link",
        "usage": "{tr}derp",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1353) to access **DerpfestOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="dot$",
    command=("dot", plugin_category),
    info={
        "header": "DotOS Post Link",
        "usage": "{tr}dot",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1269) to access **DotOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="evo$",
    command=("evo", plugin_category),
    info={
        "header": "EvolutionX Post Link",
        "usage": "{tr}evo",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1343) to access **EvolutionX** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="exthm$",
    command=("exthm", plugin_category),
    info={
        "header": "ExthmUI Post Link",
        "usage": "{tr}exthm",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1363) to access **ExTHmUI** DSBs for all ROM versions.")



@catub.cat_cmd(
    pattern="fluid$",
    command=("fluid", plugin_category),
    info={
        "header": "FluidOS Post Link",
        "usage": "{tr}fluid",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1180) to access **FluidOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="havoc$",
    command=("havoc", plugin_category),
    info={
        "header": "HavocOS Post Link",
        "usage": "{tr}havoc",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1352) to access **HavocOS** DSBs for all ROM versions.")






@catub.cat_cmd(
    pattern="kangos$",
    command=("kangos", plugin_category),
    info={
        "header": "KangOS Post Link",
        "usage": "{tr}kangos",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1354) to access **KangOS** DSBs for all ROM versions.")






@catub.cat_cmd(
    pattern="los$",
    command=("los", plugin_category),
    info={
        "header": "LineageOS Post Link",
        "usage": "{tr}los",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1251) to access **LineageOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="legion$",
    command=("legion", plugin_category),
    info={
        "header": "LegionOS Post Link",
        "usage": "{tr}legion",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1017) to access **LegionOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="para$",
    command=("para", plugin_category),
    info={
        "header": "Paranoid Android Post Link",
        "usage": "{tr}para",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1372) to access **Paranoid Android** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="posp$",
    command=("posp", plugin_category),
    info={
        "header": "POSP Post Link",
        "usage": "{tr}posp",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1445) to access **POSP** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="p404$",
    command=("p404", plugin_category),
    info={
        "header": "Project404 Post Link",
        "usage": "{tr}p404",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1122) to access **Project404** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="msmex$",
    command=("msmex", plugin_category),
    info={
        "header": "MSM Extended Post Link",
        "usage": "{tr}msmex",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1311) to access **MSM Extended** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="nezuko$",
    command=("nezuko", plugin_category),
    info={
        "header": "NezukoOS Post Link",
        "usage": "{tr}nezuko",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1448) to access **NezukoOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="nusa$",
    command=("nusa", plugin_category),
    info={
        "header": "Nusantara Project Post Link",
        "usage": "{tr}nusa",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1337) to access **Nusantara Project** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="octavi$",
    command=("octavi", plugin_category),
    info={
        "header": "OctaviOS Post Link",
        "usage": "{tr}octavi",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1348) to access **OctaviOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="sparkos$",
    command=("sparkos", plugin_category),
    info={
        "header": "SparkOS Post Link",
        "usage": "{tr}sparkos",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1121) to access **SparkOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="spice$",
    command=("spice", plugin_category),
    info={
        "header": "SpiceOS Post Link",
        "usage": "{tr}spice",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1226) to access **SpiceOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="stock$",
    command=("stock", plugin_category),
    info={
        "header": "Stock ROMs Post Link",
        "usage": "{tr}stock",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1365) to access **Stock ROMs** DSBs.")




@catub.cat_cmd(
    pattern="styx$",
    command=("styx", plugin_category),
    info={
        "header": "Styx Project Post Link",
        "usage": "{tr}styx",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1194) to access **Styx Project** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="syberia$",
    command=("syberia", plugin_category),
    info={
        "header": "SyberiaOS Post Link",
        "usage": "{tr}syberia",
    },
)
async def _(event):
    await event.edit(" [Click Here](https://t.me/DualstatusbarDSB/1175) to access **SyberiaOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="ssos$",
    command=("ssos", plugin_category),
    info={
        "header": "ShapeshiftOS Post Link",
        "usage": "{tr}ssos",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1318) to access **ShapeshiftOS** DSBs for all ROM versions.")




@catub.cat_cmd(
    pattern="pixelb$",
    command=("pixelb", plugin_category),
    info={
        "header": "Pixel-Based ROMs Post Link",
        "usage": "{tr}pixelb",
    },
)
async def _(event):
    await event.edit("[Click Here](https://t.me/DualstatusbarDSB/1285) to access **Pixel-Based ROMs** DSBs.")