#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv;

uniform sampler2D dimensionMap;
uniform sampler2D plainView;
uniform sampler2D sightView;


void main() {
    // Output fragment color

    float dim = texture(dimensionMap, uv).r;

    vec4 plainColor = texture(plainView, uv);
    vec4 sightColor = texture(sightView, uv);

    fragColor = mix(plainColor, sightColor, dim);
}