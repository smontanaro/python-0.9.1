Notes on building Python 0.9.1
==============================

A note to webmaster@python.org referred us to Guido's 0.9.1 release as
a set of shell archive files posted to alt.sources:

https://groups.google.com/g/alt.sources/search?q=%22python%200.9.1%22

I downloaded them as well as a single patch. I then made a few edits
to get the interpreter to build. The shar files as well as a single
patch file Guido posted are in this directory. Note the missing
part 02. As Guido explained:

> In case anyone wondered where the real part 02 is, it isn't needed.
> It contained a generated file of 151K that shouldn't be in the
> distribution, and I cancelled it.
> --
> Guido van Rossum, CWI, Amsterdam <gu...@cwi.nl>
> "PS I have never kissed the editor of the Radio Times"

(I have no idea what is going on in Guido's .sig. You will have to ask
him. <wink>)

The patch didn't apply for me (structural issues), so I just applied
its edits manually. I then set about getting the interpreter to
compile. That was pretty straightforward. The result is in
compile.patch in this directory.

-- Skip Montanaro - 2021-02-16
