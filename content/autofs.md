Title: Jak automaticky připojovat vzdálené diskové oddíly
Date: 2014-10-31 14:57
Category: Blog
Tags: Linux, SSH
Author: Marek Nožka

Autofs
==========

Pomocí Autofs lze zařídit automatické připojení souborového systému při jeho
prvním použití a jeho automatické odpojení při nečinnosti. Vše se děje na
základě přednastaveného mapování. Takto lze připojovat vyměnitelné médium,
Sambu nebo jakékoliv FUSE. 

O Autofs jsem se dozvěděl náhodou v jedné e-mailové konferenci, kde se řešil
úplně jiný problém. Mě při této příležitosti napadlo, že si takto můžu připojit
své vzdálené disky, které jsem zatím, připojoval ručně pomocí příkazu `sshfs`.
V tomto zápisku se tedy zaměřím na [sshfs](http://packages.debian.org/sshfs), 
ale [[!dd našel]](autofs Samba) jsem [hezký návod i pro Sambu][].

[hezký návod i pro Sambu]: http://www.howtoforge.com/accessing_windows_or_samba_shares_using_autofs
[Jak se přihlašovat na SSH bez zadávání hesla]: http://www.root.cz/clanky/jak-se-prihlasovat-na-ssh-bez-zadavani-hesla/
[Seriál Pokročilé vlastnosti OpenSSH]: http://www.root.cz/serialy/pokrocile-vlastnosti-openssh/
[OpenSSH - více než jen Secure Shell]: http://www.abclinuxu.cz/clanky/bezpecnost/openssh-vice-nez-jen-secure-shell
[OpenSSH - bezpečně a pohodlně]: https://www.abclinuxu.cz/clanky/bezpecnost/openssh-bezpecne-a-pohodlne


SSH klíče pro Roota
====================

Nejprve je třeba zajistit, aby se lokální uživatel `root` dostal ke vzdálenému
uživatelskému účtu a nemusel zapisovat heslo -- vše se má dít automaticky. To
lze zajistit pomocí SSH klíčů.

SSH a SSH klíče:
: [Seriál Pokročilé vlastnosti OpenSSH][]
: [Jak se přihlašovat na SSH bez zadávání hesla][]
: [OpenSSH - více než jen Secure Shell][]
: [OpenSSH - bezpečně a pohodlně][]

Vygenerujeme rootovi [[!enwk keypair]](). Důležité je, aby byl privátní klíč 
bez `passphrase`. Při dotazu na `passphrase` je tedy třeba zadat jen `Enter`.


    :::console
    # ssh-keygen -t dsa
    Generating public/private dsa key pair.
    Enter file in which to save the key (/root/.ssh/id_dsa):
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /root/.ssh/id_dsa.
    Your public key has been saved in /root/.ssh/id_dsa.pub.
    The key fingerprint is:
    03:ca:c2:ae:42:b8:e8:8f:85:b8:fd:2f:7b:5f:a6:7e marek@impala
    The key's randomart image is:
    +---[DSA 1024]----+
    |                 |
    |                 |
    |      .          |
    | . . . .         |
    |. o o   S        |
    |oo..     .       |
    |+o..      o      |
    |++o . .  +E      |
    |=oooo=.o+.       |
    +-----------------+


Veřejný klíč je poté třeba dopravit na vzdálený počítač do souboru
`~/.ssh/authorized_keys`. Pokud už soubor nějaké klíče obsahuje klíč se
jednoduše připojí na konec.

Toto lze zařídit mnoha způsoby. Například takto:

    :::console
    # ssh user@masina.nekde.tld 'cat >>~/.ssh/authorized_keys' <~/.ssh/id_dsa.pub

V tomto okamžiku by mělo fungovat přihlášení roota ke vzdálenému počítači bez
hesla, jen na základě klíče.

    :::console
    # ssh user@masina.nekde.tld

Přihlášení je dobré ověřit ještě před konfigurací Autofs. sshfs nebude
fungovat, pokud uživatel root nebude mít ověřenou identitu serveru. A to se
děje právě při první přihlášení pomocí SSH.


Konfigurace autofs
====================

Autofs je třeba nejprve naistalovat:

    :::console
    # aptitude install autofs sshfs

Poté vytvořím soubor s definicemi co a kam se bude připojovat. Řádky jsou
poměrně dlouhé:

`/etc/auto.sshfs`


    :::text
    masina  -fstype=fuse,allow_other,reconnect,uid=1000,gid=1000 sshfs\#user@masina.tld:/home/user
    borec   -fstype=fuse,allow_other,reconnect,uid=1000,gid=1000 sshfs\#borec@jinde.tld:/home/stud/borec

`uid` a `gid` patří uživateli, na kterého se bude připojený souborový systém
mapovat. Pokud neznáte své `uid` neznáte stačí spustit příkaz `id`.


Takto vytvořený soubor musíme zaregistrovat aby o něm Autofs věděl. To se dá
zařídit v souboru `/etc/auto.master`. Na konec jsem přidal řádek:

    :::text
    /mnt/sshfs   /etc/auto.sshfs --timeout=30

Nyní je třeba službu restartovat, aby si všimla změn, které jsme provedli v
konfiguraci.

    :::console
    # /etc/init.d/autofs restart


Jak se to používá?
===================

Jednoduše vstoupíte do adresáře `/mnt/sshfs/masina` nebo si třeba vypíšete
obsah adresáře `/mnt/sshfs/borec`. Souborový systém se automaticky připojí
jakmile na něj sáhnete. ... a po 30 sekundách, co na něj nesáhnete se
automaticky odpojí.

Mě ještě trochu točilo, že složka `/mnt/sshfs` je při odpojených vzdálených
file-systémech prázdná. Když jsem chtěl její jméno doplnit tabulátorem shell si
na tento adresář "sáhnul" a připojili se všechny oddíly. Proto jsem v souboru
`/etc/default/autofs` zapnul/odkomentoval volbu 

    :::text
    BROWSE_MODE="yes"

Tím je zařízeno, že se moje `masina` a `borec` objeví v adresáři `/mnt/sshfs`,
i když jsou odpojené.
