# Diadochi

A minimal static site generator for people who hate the web.
It is designed to be simple to understand and extend, so it probably won't meet
your needs.

See below for a list of enhanced, community-supported forks.
Use at your own risk!

| Name | Base release | Description | Status |
| ---- | ------------ | ----------- | ------ |
| [Diadochi for Neocities](https://github.com/indraj-net/diadochi-neocities) | v1 r1 | Supports custom 404 pages and CLI uploads | Active |

## Prerequisites

The target interpreter is Python 3.8 or higher.
No additional dependencies are required.

## API stability

Interfaces do not change between revisions, but may change between versions.
Revisions which rectify security flaws are issued for the most recent version
and backported to the previous version (if necessary).
Earlier versions will not receive security fixes.

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

Please ignore PEP 8 and related standards (they are terrible).
In particular, you should:

- indent using tabs rather than spaces;
- indent width should be set to 8 chars;
- line width should not exceed 80 chars unless this affects readability;
- refrain from the use of object-oriented style;
- refrain from the use of so-called design patterns; and
- refrain from catching exceptions you don't intend to handle.

### Can I rewrite this in Rust?

Sure, but I will [reject](https://indraj.net/posts/rust) your PR.
You're welcome to maintain your own version, however.

## License

Diadochi is licensed under the GNU Affero General Public License.
See COPYING.
