#version 330 core

out vec4 fragColor;

in vec2 uv;

uniform sampler2D dimensionMap;
uniform sampler2D plainView;
uniform sampler2D sightView;

void main()
{ 
    float dim = texture(dimensionMap, uv).r;
    float depth = texture(dimensionMap, uv).w;

    vec3 plain = texture(plainView, uv).rgb;
    vec3 sight = texture(sightView, uv).rgb;

    fragColor = vec4(mix(plain, sight, dim), 1.0);

    // if (depthDim > depthSight) {
    //     fragColor = vec4(plain, 1.0);
    // }
    // else {
    //     fragColor = vec4(mix(plain, sight, dim), 1.0);
    // }

    // fragColor.rgb /= 100000;

    // if 

    // fragColor.rgb += 20 - depthSight * 20;
    // fragColor.r += 20 - depthDim * 20;

}