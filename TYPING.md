This fork adds adjacent PEP 561 stubs and uses standard project metadata so an
ordinary source installation works with Flit 4. The serialization implementation
and executable test statements are unchanged. The distribution version is
`3.1.2+stablekite.2`.

The signatures cover the package exports, public implementation helpers, and the
legacy `cloudpickle_fast` module. Known parameters retain their types: binary
streams, integer protocols, `PickleBuffer` callbacks, and module registrations.
`Pickler` remains a subclass of the standard `pickle.Pickler`. Its actual
`reducer_override(obj=...)` hook explicitly returns a documented reduction or
`NotImplemented`; the signature preserves the supported keyword argument.
Six-element reductions include the optional two-argument state setter. These
contracts require the corresponding corrected standard-library stubs in the
StableKite MyPy and Pyright native-typing-contracts-v2 builds. The signatures
retain rejection of invalid reductions and do not change serialization code.

`load` and `loads` are the actual standard-library functions and are re-exported
directly. Their decoded result cannot be determined from the input bytes; the
standard dynamic result is preserved. No assertion that unpickling returns the
original object's static type is introduced. Reduction callback payloads likewise
use the existing standard-library pickle contract rather than a universal new
fallback type.

The original Black 23.9.1 hook rejects `py313` in the original target list. The
redundant unsupported entry is removed; the minimum syntax target remains
Python 3.8. One original overlong test comment is wrapped without changing its
AST, assertions, inputs, or expected results. These changes allow the existing
style checks to run without ignoring diagnostics or replacing the pinned tools.

The known-field constructor work and ctypes stub changes in other repositories
are separate. This package does not configure the caller's checking rules or
replace any caller implementation.

Full Pyright type-completeness remains limited by public re-exports from the
standard library, including the existing dynamic NotImplementedType boundary.
No public names are hidden and no external types or checking rules are weakened
to claim a complete score. Runtime stubtest and direct strict API checks are
qualified separately.
