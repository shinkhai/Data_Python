# Password Manager
![](https://images.unsplash.com/photo-1522251670181-320150ad6dab?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=9ffb5fa03315c9a9674fe4ef0aee552e&auto=format&fit=crop&w=1000&q=80)

Having the same password on every website or app is a very bad idea. Anyone who
can get your password on one of these services will have access to all the
others.  
In order to avoid this issue, there exist services that can help you manage
your passwords by:
1. securely storing them
1. generating strong randomly generated password

In this assigment, you'll implement your own password manager that will focus on `1`, e.g. generating password.

NB: this is a toy project, handling passwords securely is actually a very
difficult thing to achieve.

## Guidelines

We'll build 2 classes for this:
* `PasswordRecord`
* `PasswordManager`

But first, we need to implement a function, `generate_password`, that will help
us generate passwords when we need them.

You'll write all of these in the `src/password_manager.py` file.

### `generate_password`
Takes an optional parameter `n_characters` (default to 20) which will be the
length of the generated password.  
The function should return a string of length `n_characters` where each
character was randomly generated.


### `PasswordRecord`
This class will be used to store and link website's url to passwords.
It takes 2 arguments, where one is optional:
* `url`: the url of the service (website or app)
* `password`: optional, if none is given, you'll have to generate a password
  using `generate_password`


### `PasswordManager`
This class will store and keep track of the passwords.

It should implement an attribute `passwords` (accessible via `self.passwords`),
a list of all the passwords saved (we'll let you decided how this should be
initialized).

It should also implement an instance method `add_password` that takes a single
argument `value`, then:
* if `value` is a `PasswordRecord` object, it should add this record to the
passwords list.
* if `value` is not a `PasswordRecord` object, we'll consider value is probably
  a URL and our user want us to generate a password for him. We'll then create
  a `PasswordRecord` object with the URL and a randomly generated password
  using the `generate_password` function. You'll then add this new
  `PasswordRecord` object to the passwords list of our `PasswordManager`.

Then, the method will return the value of the password to the user.
