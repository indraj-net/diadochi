# Diadochi

A minimal static site generator for Neocities.

## Prerequisites

The Digital Mars D compiler (dmd) package from [dlang.org](https://dlang.org/).

## Build

```
dub build --build=release
```

## API stability

Diadochi releases now follow the [SemVer](https://semver.org/) specification.

## Report a bug

To report a security bug, send me an email.
My contact details are available on my GitHub profile or via my
[website](https://indraj.net).
Please allow up to 48 hours for a reply, and up to 90 days for the issue to be
confirmed and fixed before disclosing it publicly.

For all other bugs, open an issue.

## Contributing

Thank you for your interest in contributing to Diadochi!

Before submitting a PR, please open an issue to discuss your proposed changes.
All contributions are subject to the
[Developer Certificate of Origin (DCO)](https://developercertificate.org/).
By signing off on your commit(s), you are agreeing to be bound by the DCO.
Commits without sign-off will be rejected.
For the purposes of copyright provenance and transparency, you must use your
full, legal name and a non-temporary email address.

### Coding style

Please adhere to the kernel coding standards as far as possible.
In particular:

- indent using tabs rather than spaces;
- indent width should be set to 8 chars; and
- line width should not exceed 80 chars unless this affects readability.

D-specific guidelines:

- refrain from writing your own classes, interfaces and templates.

### Can I rewrite this in Rust?

Sure, but I will [reject](https://indraj.net/posts/rust) your PR.
You're welcome to maintain your own version, however.

## License

Diadochi is licensed under the GNU Affero General Public License.
See COPYING.
