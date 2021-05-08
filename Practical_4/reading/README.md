# Collaboration I

## Communications channels

### Exercise: Write a simple RFC561-compliant e-mail.

From: denis@hse.ru
To: nick@hse.ru
Date: 07 APR 2021 1527-MSK
Subject: Homework assignment

This is a simple RFC561-compliant e-mail

Best regards,
Denis

### Exercise: Send yourself an e-mail with non-ASCII characters. (E.g., "привет!") Download the raw message and open with a text editor. What are the contents? How is the message encoded, and where is the encoding specified? (Sometimes you need to select "view message source" or "view original message" to do this.)

Each field containing Russian characters has the following prefix `?koi8-r?B?`
Additionally, there are such fields as `Accept-Language: ru-RU, en-US` and `Content-Language: ru-RU`

First of all, it has the `X-MS-Has-Attach: yes` field.
Its `Content-Type` is application/ms-tnef;

### Exercise: How are attachments handled? Refer to the Wikipedia article on MIME; send yourself an e-mail with a (very small!) attachment, and download the raw e-mail message and open with a text editor. What are the contents? Show and explain each MIME part. Can you recover the attachment from the raw message?

`MIME-Version: 1.0` - an indicator of MIME formatting

`Content-Transfer-Encoding: quoted-printable` - describes the encoding type to be applied before reading the original content of the email (text).

`Content-Transfer-Encoding: base64` - describes the encoding type to be applied before getting the original attachment of the email.

`Content-Type: application/octet-stream; name="test.sql"` - describes the attahced file

## IRC

### Exercise: Install an IRC client, log in to freenode.net, join #apertium and write a message "begiak: tell nlhowell hi". It will instruct the bot managing #apertium to forward me the message next time it sees me.

<dmkapel> begiak: tell nlhowell hi
<begiak> dmkapel: I'll pass that on when nlhowell is around.

## Quality control

### Exercise: Both Python and the Linux kernel have considered in the past moving from bugzilla- and e-mail-based systems to forges. Read both articles, and summarise the advantages and disadvantages of forge-based systems and e-mail, and the results of each.

Advantages of forge-based systems and e-mail:
* It is possible to arrange notifications in a desired order, not the one that was suggested by the system
* General independace from large solution-providers
* More flexible and suitable for large projects

Disadvantages of forge-based systems and e-mail:
* It complicates things for new contributors.
* Resources have to be allocated to keep it running
* Lacks some functionality that bug-tracking platforms provide out of the box

### Exercise: Suppose your project is not software. What kinds of quality control tests might you implement? Give examples for written articles, web sites, musical compositions, and graphics.

* written articles: Spellchecking. Check for the length of paragraphs and sentencens to highlight those that are too long.
* web sites: Test the connection. Test on web accesibility.
* musical compositions: it usually has a certain pattern, especially pop music, every 32 beats the music has to change, at least slightly. Also, it terms of genres, each piece of music has its conventional bps. Test if a given bps rate corresponds to a desired genre.
* graphics: test the rgb values on being too bright, or the number of rgb triples is too many.

### Exercise: install and run pandoc. (The dependencies are hefty.)

Setting up pandoc (2.5-3build2) ...
Processing triggers for man-db (2.9.1-1) ...
