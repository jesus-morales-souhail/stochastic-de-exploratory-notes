# Car + drone at 120 km/h: pupil diffraction under Newton and Einstein

**Author:** Jesús Morales Souhail  
**Date:** July 2026  
**Status:** Quantitative thought experiment (no tesseract)  
**Script:** `scripts/car_drone_pupil_newton_einstein.py`  
**Related:** `papers/self-shielding-vs-untestability.md`, `papers/no-go-superoscillation-tesseract.md`

---

## Setup

I wanted a clean local experiment that people sometimes try to load with cosmology. The setup is simple:

- A car on a highway at constant speed \(v = 120\,\mathrm{km/h}\).
- A drone flying parallel at the same velocity, so the relative velocity between car and drone is zero.
- Inside the car: diffraction of light (\(\lambda = 550\,\mathrm{nm}\)) through an aperture \(D = 1\,\mathrm{mm}\) (a “1 mm pupil”), also compared with a 4 mm human pupil.

The question I ask is whether the Airy pattern changes under Newton versus Einstein, and whether cosmic expansion shows up at all.

I deliberately leave out hypercubes, Coxeter \(B_4\), and any undeclared 4D optical engine.

---

## Premises I am using

1. **EM rigidity.** Electromagnetic binding in atoms and solids is enormously stronger than Hubble tidal effects on human or car scales. Local bound systems do not expand with the Hubble flow.
2. **Inertial frames.** Constant velocity means no acceleration, so Galilean / special-relativistic inertial physics applies. For the passenger, a closed car is essentially a lab at rest.

---

## Results (from the script)

### A) Expansion versus local binding

$$
H_0 \sim 2\times 10^{-18}\,\mathrm{s}^{-1} \qquad\Rightarrow\qquad v_H = H_0 L
$$

| \(L\) | \(v_H = H_0 L\) |
|-------|-----------------|
| \(10^{-10}\,\mathrm{m}\) (atom) | \(\sim 10^{-28}\,\mathrm{m/s}\) |
| \(1\,\mathrm{m}\) | \(\sim 10^{-18}\,\mathrm{m/s}\) |
| \(10^{6}\,\mathrm{m}\) | \(\sim 10^{-12}\,\mathrm{m/s}\) |

Over 60 s, the stretch of a 1 m length is \(\Delta L \sim 10^{-16}\,\mathrm{m}\). That is irrelevant next to atomic sizes fixed by electromagnetism.

### B) Diffraction (car rest frame)

Airy angle to the first minimum: \(\theta \approx 1.22\,\lambda/D\).

| \(D\) | \(\theta\) | Airy radius on \(f\approx 17\,\mathrm{mm}\) |
|-------|------------|-----------------------------------------------|
| 1 mm | \(\sim 6.7\times 10^{-4}\,\mathrm{rad}\) | \(\sim 11\,\mu\mathrm{m}\) |
| 4 mm | \(\sim 1.7\times 10^{-4}\,\mathrm{rad}\) | \(\sim 2.9\,\mu\mathrm{m}\) |

### C) Newton / Galileo

With car and drone co-moving, relative velocity is zero. The passenger and the drone see the same local diffraction geometry. I do not need an absolute-space story about “diagonal light plus \(v\)” between them; they share a rest frame.

### D) Einstein (special relativity)

$$
\beta = \frac{v}{c} \approx 1.1\times 10^{-7},\qquad \gamma-1 \approx 6\times 10^{-15}.
$$

- **Correct setup** (matched velocities): relative \(\beta = 0\), so no contraction or Doppler between car and drone, and the Airy pattern is identical.
- **Wrong setup** (drone fixed to the road): aberration is \(\sim\beta\) rad \(\approx 0.023''\), while the Airy angle is \(\sim 138''\) for 1 mm, so \(\beta/\theta_{\mathrm{Airy}}\sim 10^{-4}\). That is undetectable as any “tesseract-like” distortion of the pupil pattern.

### E) When SR would matter optically

Aberration comparable to the Airy angle at 1 mm needs \(v \sim \theta c \approx 200\,\mathrm{km/s}\) (about \(6000\times\) 120 km/h).  
\(\gamma-1\sim 1\%\) needs \(v\sim 0.14\,c\).

### F) Cosmological expansion during the drive

Expansion is not a 4D optical effect in the pupil. I measure it with the redshift of free photons over gigaparsec baselines, not with a 1 mm aperture at highway speed.

---

## Link to “the question the mechanism blinds”

| Local car / pupil | Cosmology (SDiff / \(\sigma_X\)) |
|-------------------|----------------------------------|
| EM binds matter against Hubble flow | SDiff projects isotropic vacuum stress \(\propto g_{\mu\nu}\) |
| Wrong scale for expansion | Wrong operator for a generic “does the vacuum tremble?” |
| Measure free light over cosmic baselines | Measure residuals / slip / specific models with amplitudes |

The “shield” here is ordinary local physics at the right scale, not magic immunity forever. The blinded question is mis-scaled; it is not that physics fails inside the car.

---

## Conclusion

1. **Newton (co-moving):** same diffraction inside the car and for the drone.
2. **Einstein (co-moving):** same; relative rest.
3. **Einstein (drone on the road):** SR corrections \(\sim 10^{-15}\)–\(10^{-7}\), negligible versus Airy.
4. **No tesseract** appears in any consistent calculation at 120 km/h.
5. Same methodological rule as Option 0 and the optics no-gos: derive the map, quote the amplitude, or do not claim the effect.

Run: `python scripts/car_drone_pupil_newton_einstein.py`

---

## Status: CLOSED

I lock this result as testing **local EM diffraction plus inertial SR at** \(\beta\sim 10^{-7}\).  
It does **not** test cosmic expansion or any tesseract optical engine.

| Diagnosis | Content |
|-----------|---------|
| Wrong **scale** | Hubble / cosmic geometry on millimetre–metre lengths and seconds |
| Wrong **operator** | Pupil Airy pattern (and non-derived 4D “projection”) |

For next experiments I only want those with **correct scale and correct operator** — see `papers/scale-operator-experiment-map.md`.
