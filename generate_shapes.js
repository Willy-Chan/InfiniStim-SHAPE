// failed experiment, simply for the fact that we can't generate such images in a ROAR setting
// due to the requirement of server processing. Will have to speak to Adam or Elijah for further experimentation
// in this task.

// completing this would essentially allow for infinite stimuli to be generated!

const fs = require('fs');
const sharp = require('sharp');
const shuffleArray = require('shuffle-array');

async function flipImage(imageBuffer, axis) {
  let image = sharp(imageBuffer);
  if (axis === 'x') {
    image = await image.flip().toBuffer();
  } else if (axis === 'y') {
    image = await image.flop().toBuffer();
  } else if (axis === 'both') {
    image = await image.flip().flop().toBuffer();
  }
  return image;
}

// eslint-disable-next-line import/prefer-default-export
export async function combineImages(folderPath, outputPath, imageFile1, imageFile2, imageFile3, imageFile4) {
  // Array of specified images
  const imageFiles = [imageFile1, imageFile2, imageFile3, imageFile4];

  const images = [];
  const partNumbers = [];

  // Iterate through specified image files
  for (const imageFile of imageFiles) {
    const imagePath = `${folderPath}/${imageFile}`;
    const imageBuffer = fs.readFileSync(imagePath);
    images.push(await sharp(imageBuffer).toBuffer());

    // Extract the part number from the image filename
    const partNumber = imageFile.split('_').pop().split('.')[0];
    partNumbers.push(partNumber);
  }

  const { width, height } = await sharp(images[0]).metadata();
  const canvas = sharp({
    create: {
      width: width * 2,
      height: height * 2,
      channels: 4,
      background: { r: 0, g: 0, b: 0, alpha: 0 },
    }
  });

  const positions = [{ left: 0, top: 0 }, { left: width, top: 0 }, { left: 0, top: height },
  { left: width, top: height }];
  const flipAxes = [null, 'y', 'x', 'both'];

  let imageComposites = [];
  for (let i = 0; i < images.length; i++) {
    const flipAxis = flipAxes[i];
    let imageBuffer;
    if (flipAxis) {
      imageBuffer = await flipImage(images[i], flipAxis);
    } else {
      imageBuffer = images[i];
    }
    imageComposites.push({
      input: imageBuffer,
      top: positions[i].top,
      left: positions[i].left
    });
  }

  await canvas.composite(imageComposites).toFile(`${outputPath}/${partNumbers.join('_')}.png`);
  console.log(`Full image created and saved as ${outputPath}/${partNumbers.join('_')}.png`);
  return `${outputPath}/${partNumbers.join('_')}.png`; // Return the filename
}

// Use the function with specific images
combineImages(
  './assets/shape_components',
  './assets/ai_by_parts',
  '1.png',
  '2.png',
  '3.png',
  '4.png'
);

// OLD CODE: GENERATE THE IMAGES FROM PARTS FROM WITHIN THE BROWSER:
// store.session.set("parts_folder", './assets/shape_components');
// store.session.set("output_folder", './assets/single_ai_trial');

// function hasOverlap(arr1, arr2) {
//   return arr1.some(val => arr2.includes(val));
// }

// function getNUniqueRandomIntsExclude(min_val, max_val, n, exclude) {
//   let nums = [];
//   while (nums.length < n) {
//     const randomNum = getRandomIntInclusive(min_val, max_val);
//     if (!nums.includes(randomNum) && !exclude.includes(randomNum)) {
//       nums.push(randomNum);
//     }
//   }
//   return nums;
// }

// const getAIpartsStimulus = () => {
//   store.session.set("trial_type", getRandomMatchNonMatch());

//   if (store.session("trial_type") === 'nonmatch') {
//     store.session.set("difficulty_index", getRandomIntInclusive(0, 3));
//     const difficulty_index = store.session("difficulty_index");
//     const partOptions1 = getNUniqueRandomInts(1, 12, 4); // Get first 4 parts
//     let partOptions2 = [];

//     if (difficulty_index === 0) {
//       do {
//         partOptions2 = getNUniqueRandomInts(1, 12, 4); // Get next 4 parts
//       } while (hasOverlap(partOptions1, partOptions2)); // Ensure no overlap
//     } else {
//       // Parts that will overlap
//       const overlappingParts = getNUniqueRandomInts(1, 12, difficulty_index);
//       // Get parts that won't overlap
//       const uniqueParts = getNUniqueRandomIntsExclude(1, 12, 4 - difficulty_index, [...partOptions1,
//         ...overlappingParts]);
//       partOptions2 = [...overlappingParts, ...uniqueParts]; // Combine to form second set of parts
//     }

//     let green = combineImages(store.session("parts_folder"), store.session("output_folder"), partOptions1[0], partOptions1[1], partOptions1[2], partOptions1[3]);
//     let white = combineImages(store.session("parts_folder"), store.session("output_folder"), partOptions2[0], partOptions2[1], partOptions2[2], partOptions2[3]);
//     let red = white;

//     store.session.set("red", red);
//     store.session.set("white", white);
//     store.session.set("green", green);
//   } else if (store.session("trial_type") === 'match') {
//     store.session.set("difficulty_index", -1);
//     console.log(store.session("difficulty_index"));
//     const partOptions = getNUniqueRandomInts(1, 12, 4);

//     let red = combineImages(store.session("parts_folder"), store.session("output_folder"), partOptions[0], partOptions[1], partOptions[2], partOptions[3]);
//     let white = combineImages(store.session("parts_folder"), store.session("output_folder"), partOptions[0], partOptions[1], partOptions[2], partOptions[3]);
//     let green = white;

//     store.session.set("red", red);
//     store.session.set("white", white);
//     store.session.set("green", green);
//   }
// };