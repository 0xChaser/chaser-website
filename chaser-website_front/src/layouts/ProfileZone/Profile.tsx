import React from 'react';
import { Box, Flex, Image, Heading, Text, useColorModeValue } from "@chakra-ui/react";
import ProfileBg from "../../components/pictures/profile_bg.png";
import chaserPicture from "../../components/pictures/chaser-picture.png";

const ProfileLayout: React.FC = () => {
    const bgOverlayColor = useColorModeValue("rgba(0, 0, 0, 0.6)", "rgba(0, 0, 0, 0.7)");

    return (
        <Box
            w="100vw"
            h="100vh"
            backgroundImage={`url(${ProfileBg})`}
            backgroundSize="cover"
            backgroundPosition="center"
            position="relative"
            display="flex"
            alignItems="center"
            justifyContent="center"
            _before={{
                content: '""',
                position: "absolute",
                top: 0,
                left: 0,
                width: "100%",
                height: "100%",
                backgroundColor: bgOverlayColor,
                zIndex: 1,
            }}
        >
            <Flex
                position="relative"
                zIndex={2}
                h="100%"
                direction={["column", "column", "row"]}
                align="center"
                justify="space-between"
                px={[6, 12, 16]}
                maxW="1200px"
                w="100%"
            >
                <Image
                    src={chaserPicture}
                    boxSize={["150px", "200px", "250px"]}
                    borderRadius="full"
                    filter="grayscale(100%)"
                    alt="Profile"
                    mb={[4, 0]}
                />
                <Box
                    textAlign={["center", "center", "right"]}
                    maxW="60%"
                    color="white"
                    ml={[0, 0, 8]}
                >
                    <Heading as="h1" fontSize={["2xl", "3xl", "4xl"]} mb={4}>
                        Florian ISAK
                    </Heading>
                    <Text fontSize={["md", "lg", "xl"]}>
                        Fullstack Developer avec une passion pour créer des solutions web innovantes et performantes. Je suis spécialisé en React, Node.js, et TypeScript. Toujours à l'affût des nouvelles technologies, je m'efforce de construire des applications robustes et évolutives.
                    </Text>
                </Box>
            </Flex>
        </Box>
    );
};

export default ProfileLayout;